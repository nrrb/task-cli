from datetime import datetime
import uuid


class Task:

    def __init__(self, description, id=None, status=None, createdAt=None, updatedAt=None):
        self.description = description
        self.id = id or str(uuid.uuid4())[:5]
        self.status = status or 'to-do'
        self.createdAt = createdAt or datetime.now()
        self.updatedAt = updatedAt or datetime.now()

    def update_timestamp(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)  # Execute the original method
            self.updatedAt = datetime.now()  # Update the updatedAt timestamp
            return result
        return wrapper

    def __str__(self):
        return f"{self.id}: {self.description} ({self.status}) (A: {self.createdAt} - U: {self.updatedAt})"

    @update_timestamp
    def update_description(self, new_description):
        self.description = new_description
