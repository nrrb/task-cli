from datetime import datetime
import uuid


class Task:

    def __init__(self,
                 description: str,
                 id: str|None = None,
                 status: str|None = None,
                 createdAt: str|None = None,
                 updatedAt: str|None = None):
        self.description = description
        self.id = id or str(uuid.uuid4())[:5]
        self.status = status or 'to-do'
        self.createdAt = createdAt or datetime.now()
        self.updatedAt = updatedAt or datetime.now()

    def update_timestamp(func: callable) -> callable:
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)  # Execute the original method
            self.updatedAt = datetime.now()
            return result
        return wrapper

    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.status}) (A: {self.createdAt} - U: {self.updatedAt})"

    @update_timestamp
    def update_description(self, new_description: str):
        self.description = new_description
