from .task import Task
import json


class TaskEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Task):
            return {
                "id": obj.id,
                "description": obj.description,
                "status": obj.status,
                "createdAt": obj.createdAt.isoformat(), # Make the JSON human-readable
                "updatedAt": obj.updatedAt.isoformat()
            }
        return super().default(obj)