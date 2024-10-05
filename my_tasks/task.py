from datetime import datetime
import uuid


class Task:

    def __init__(self, description, id=None, status=None, createdAt=None, updatedAt=None):
        self.description = description
        self.id = id or str(uuid.uuid4())[:5]
        self.status = status or 'to-do'
        self.createdAt = createdAt or datetime.now()
        self.updatedAt = updatedAt or datetime.now()

    def __str__(self):
        return f"{self.id}: {self.description} ({self.status}) (A: {self.createdAt} - U: {self.updatedAt})"