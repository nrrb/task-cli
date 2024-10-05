from datetime import datetime
import uuid


class Task:

    def __init__(self, description, id=None, status=None, createdAt=None, updatedAt=None):
        self.description = description
        if id is None:
            unique_id = uuid.uuid4()
            self.id = str(unique_id)[:5]
        else:
            self.id = id
        if status is None:
            self.status = 'to-do'
        else:
            self.status = status
        if createdAt is None:
            self.createdAt = datetime.now()
        else:
            self.createdAt = createdAt
        if updatedAt is None:
            self.updatedAt = datetime.now()
        else:
            self.updatedAt = updatedAt
