import json
import uuid
from typing import Any, Optional, List, Callable
from aioredis import Redis
from src.core.interfaces.queue_manager import IQueueManager
from src.core.entities.project import Project

class RedisQueueManager(IQueueManager):
    def __init__(self, redis: Redis, queue_key: str = "project_generation_queue"):
        self.redis = redis
        self.queue_key = queue_key
        self.callbacks = {}

    async def enqueue_task(self, project: Project) -> str:
        task_id = str(uuid.uuid4())
        task_data = {
            "task_id": task_id,
            "project_id": project.id,
            "status": "pending"
        }
        await self.redis.rpush(self.queue_key, json.dumps(task_data))
        await self.redis.hset(f"task:{task_id}", mapping=task_data)
        return task_id

    async def dequeue_task(self) -> Optional[Project]:
        task_data = await self.redis.lpop(self.queue_key)
        if task_data:
            task = json.loads(task_data)
            await self.update_task_status(task['task_id'], "processing")
            # Here you would typically fetch the full project data from your database
            # For this example, we'll just return a dummy Project object
            return Project(id=task['project_id'], name="Dummy Project", description="")
        return None

    async def get_queue_status(self) -> dict:
        queue_length = await self.redis.llen(self.queue_key)
        processing_tasks = await self.redis.scard("processing_tasks")
        return {
            "pending_tasks": queue_length,
            "processing_tasks": processing_tasks
        }

    async def get_task_status(self, task_id: str) -> str:
        status = await self.redis.hget(f"task:{task_id}", "status")
        if status is None:
            raise ValueError(f"Task {task_id} not found")
        return status.decode('utf-8')

    async def update_task_status(self, task_id: str, status: str) -> None:
        if not await self.redis.hexists(f"task:{task_id}", "status"):
            raise ValueError(f"Task {task_id} not found")
        await self.redis.hset(f"task:{task_id}", "status", status)
        if status == "processing":
            await self.redis.sadd("processing_tasks", task_id)
        elif status in ["completed", "failed"]:
            await self.redis.srem("processing_tasks", task_id)
        await self._trigger_callback(f"task_{status}", task_id)

    async def cancel_task(self, task_id: str) -> bool:
        status = await self.get_task_status(task_id)
        if status != "pending":
            raise ValueError(f"Task {task_id} is not cancellable")
        await self.redis.lrem(self.queue_key, 1, task_id)
        await self.update_task_status(task_id, "cancelled")
        return True

    async def retry_failed_task(self, task_id: str) -> bool:
        status = await self.get_task_status(task_id)
        if status != "failed":
            raise ValueError(f"Task {task_id} is not in a failed state")
        task_data = await self.redis.hgetall(f"task:{task_id}")
        await self.redis.rpush(self.queue_key, json.dumps(task_data))
        await self.update_task_status(task_id, "pending")
        return True

    async def register_callback(self, event: str, callback: Callable[[str, Any], None]) -> None:
        self.callbacks[event] = callback

    async def get_queue_length(self) -> int:
        return await self.redis.llen(self.queue_key)

    async def get_pending_tasks(self, limit: int = 10) -> List[dict]:
        tasks = await self.redis.lrange(self.queue_key, 0, limit - 1)
        return [json.loads(task) for task in tasks]

    async def clear_queue(self) -> int:
        pipeline = self.redis.pipeline()
        pipeline.llen(self.queue_key)
        pipeline.delete(self.queue_key)
        results = await pipeline.execute()
        return results[0]

    async def _trigger_callback(self, event: str, task_id: str, data: Any = None) -> None:
        if event in self.callbacks:
            await self.callbacks[event](task_id, data)