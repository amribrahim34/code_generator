import json
import uuid
from typing import Any, Optional, List, Callable
from datetime import datetime
import aioredis
from src.core.interfaces.queue_manager import IQueueManager
from src.core.entities.project import Project

class QueueService(IQueueManager):
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(redis_url, decode_responses=True)
        self.queue_key = "project_generation_queue"
        self.task_key_prefix = "task:"
        self.callbacks = {}

    async def enqueue_task(self, project: Project) -> str:
        task_id = str(uuid.uuid4())
        task_data = {
            "task_id": task_id,
            "project_id": project.id,
            "status": "pending",
            "enqueue_time": datetime.utcnow().isoformat()
        }
        
        async with self.redis.pipeline(transaction=True) as pipe:
            await pipe.rpush(self.queue_key, task_id)
            await pipe.hset(f"{self.task_key_prefix}{task_id}", mapping=task_data)
            await pipe.execute()
        
        return task_id

    async def dequeue_task(self) -> Optional[Project]:
        task_id = await self.redis.lpop(self.queue_key)
        if not task_id:
            return None
        
        task_data = await self.redis.hgetall(f"{self.task_key_prefix}{task_id}")
        if not task_data:
            return None
        
        await self.update_task_status(task_id, "processing")
        
        # Here you would typically fetch the full Project object from your database
        # For this example, we'll create a minimal Project object
        return Project(id=int(task_data["project_id"]))

    async def get_queue_status(self) -> dict:
        pending_tasks = await self.redis.llen(self.queue_key)
        processing_tasks = await self.redis.scard("processing_tasks")
        completed_tasks = await self.redis.scard("completed_tasks")
        failed_tasks = await self.redis.scard("failed_tasks")
        
        return {
            "pending_tasks": pending_tasks,
            "processing_tasks": processing_tasks,
            "completed_tasks": completed_tasks,
            "failed_tasks": failed_tasks
        }

    async def get_task_status(self, task_id: str) -> str:
        status = await self.redis.hget(f"{self.task_key_prefix}{task_id}", "status")
        if not status:
            raise ValueError(f"Task with ID {task_id} not found")
        return status

    async def update_task_status(self, task_id: str, status: str) -> None:
        exists = await self.redis.exists(f"{self.task_key_prefix}{task_id}")
        if not exists:
            raise ValueError(f"Task with ID {task_id} not found")
        
        await self.redis.hset(f"{self.task_key_prefix}{task_id}", "status", status)
        
        if status == "processing":
            await self.redis.sadd("processing_tasks", task_id)
        elif status == "completed":
            await self.redis.smove("processing_tasks", "completed_tasks", task_id)
            await self._trigger_callback("task_completed", task_id)
        elif status == "failed":
            await self.redis.smove("processing_tasks", "failed_tasks", task_id)
            await self._trigger_callback("task_failed", task_id)

    async def cancel_task(self, task_id: str) -> bool:
        status = await self.get_task_status(task_id)
        if status != "pending":
            raise ValueError(f"Task with ID {task_id} is not cancellable (status: {status})")
        
        async with self.redis.pipeline(transaction=True) as pipe:
            await pipe.lrem(self.queue_key, 0, task_id)
            await pipe.delete(f"{self.task_key_prefix}{task_id}")
            result = await pipe.execute()
        
        return result[0] > 0

    async def retry_failed_task(self, task_id: str) -> bool:
        status = await self.get_task_status(task_id)
        if status != "failed":
            raise ValueError(f"Task with ID {task_id} is not in a failed state (status: {status})")
        
        async with self.redis.pipeline(transaction=True) as pipe:
            await pipe.srem("failed_tasks", task_id)
            await pipe.rpush(self.queue_key, task_id)
            await pipe.hset(f"{self.task_key_prefix}{task_id}", "status", "pending")
            result = await pipe.execute()
        
        return result[1] > 0

    async def register_callback(self, event: str, callback: Callable[[str, Any], None]) -> None:
        self.callbacks[event] = callback

    async def _trigger_callback(self, event: str, task_id: str, data: Any = None) -> None:
        callback = self.callbacks.get(event)
        if callback:
            await callback(task_id, data)

    async def get_queue_length(self) -> int:
        return await self.redis.llen(self.queue_key)

    async def get_pending_tasks(self, limit: int = 10) -> List[dict]:
        task_ids = await self.redis.lrange(self.queue_key, 0, limit - 1)
        tasks = []
        for task_id in task_ids:
            task_data = await self.redis.hgetall(f"{self.task_key_prefix}{task_id}")
            tasks.append(task_data)
        return tasks

    async def clear_queue(self) -> int:
        async with self.redis.pipeline(transaction=True) as pipe:
            await pipe.llen(self.queue_key)
            await pipe.delete(self.queue_key)
            result = await pipe.execute()
        
        return result[0]  # Return the number of tasks that were in the queue

    # Additional helper methods

    async def get_task_details(self, task_id: str) -> dict:
        task_data = await self.redis.hgetall(f"{self.task_key_prefix}{task_id}")
        if not task_data:
            raise ValueError(f"Task with ID {task_id} not found")
        return task_data

    async def get_failed_tasks(self, limit: int = 10) -> List[dict]:
        task_ids = await self.redis.smembers("failed_tasks")
        tasks = []
        for task_id in list(task_ids)[:limit]:
            task_data = await self.redis.hgetall(f"{self.task_key_prefix}{task_id}")
            tasks.append(task_data)
        return tasks

    async def get_processing_tasks(self, limit: int = 10) -> List[dict]:
        task_ids = await self.redis.smembers("processing_tasks")
        tasks = []
        for task_id in list(task_ids)[:limit]:
            task_data = await self.redis.hgetall(f"{self.task_key_prefix}{task_id}")
            tasks.append(task_data)
        return tasks