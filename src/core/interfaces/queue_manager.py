from abc import ABC, abstractmethod
from typing import Any, Optional, List, Callable
from src.core.entities.project import Project

class IQueueManager(ABC):
    @abstractmethod
    async def enqueue_task(self, project: Project) -> str:
        """
        Add a project generation task to the queue.

        Args:
            project (Project): The project to be generated.

        Returns:
            str: A unique task ID for the enqueued task.
        """
        pass

    @abstractmethod
    async def dequeue_task(self) -> Optional[Project]:
        """
        Remove and return the next task from the queue.

        Returns:
            Optional[Project]: The next project to be generated, or None if the queue is empty.
        """
        pass

    @abstractmethod
    async def get_queue_status(self) -> dict:
        """
        Get the current status of the queue.

        Returns:
            dict: A dictionary containing queue statistics (e.g., pending tasks, processing tasks).
        """
        pass

    @abstractmethod
    async def get_task_status(self, task_id: str) -> str:
        """
        Get the status of a specific task.

        Args:
            task_id (str): The unique ID of the task.

        Returns:
            str: The current status of the task (e.g., 'pending', 'processing', 'completed', 'failed').

        Raises:
            ValueError: If the task ID is not found.
        """
        pass

    @abstractmethod
    async def update_task_status(self, task_id: str, status: str) -> None:
        """
        Update the status of a specific task.

        Args:
            task_id (str): The unique ID of the task.
            status (str): The new status of the task.

        Raises:
            ValueError: If the task ID is not found.
        """
        pass

    @abstractmethod
    async def cancel_task(self, task_id: str) -> bool:
        """
        Cancel a pending task in the queue.

        Args:
            task_id (str): The unique ID of the task to cancel.

        Returns:
            bool: True if the task was successfully cancelled, False otherwise.

        Raises:
            ValueError: If the task ID is not found or the task is not cancellable.
        """
        pass

    @abstractmethod
    async def retry_failed_task(self, task_id: str) -> bool:
        """
        Retry a failed task.

        Args:
            task_id (str): The unique ID of the failed task to retry.

        Returns:
            bool: True if the task was successfully queued for retry, False otherwise.

        Raises:
            ValueError: If the task ID is not found or the task is not in a failed state.
        """
        pass

    @abstractmethod
    async def register_callback(self, event: str, callback: Callable[[str, Any], None]) -> None:
        """
        Register a callback function for specific queue events.

        Args:
            event (str): The event to register the callback for (e.g., 'task_completed', 'task_failed').
            callback (Callable[[str, Any], None]): The callback function to be called when the event occurs.
                The callback should accept a task ID and optional data.
        """
        pass

    @abstractmethod
    async def get_queue_length(self) -> int:
        """
        Get the current length of the queue.

        Returns:
            int: The number of tasks currently in the queue.
        """
        pass

    @abstractmethod
    async def get_pending_tasks(self, limit: int = 10) -> List[dict]:
        """
        Get a list of pending tasks.

        Args:
            limit (int): The maximum number of tasks to return (default: 10).

        Returns:
            List[dict]: A list of dictionaries containing task information (e.g., task ID, project ID, enqueue time).
        """
        pass

    @abstractmethod
    async def clear_queue(self) -> int:
        """
        Clear all pending tasks from the queue.

        Returns:
            int: The number of tasks that were removed from the queue.
        """
        pass