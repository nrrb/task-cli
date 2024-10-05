#!/bin/python3
from datetime import datetime
import json
import os
import sys
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


class CommandLineHandler:

    def __init__(self):
        self.acceptable_verbs = ['add']
        self.file = 'tasks.json'
        self.tasks = []
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                json.dump([], f)
        with open(self.file, 'r') as f:
            tasks = json.load(f)
            for task in tasks:
                self.tasks.append(Task(
                        description = task['description'],
                        id = task['id'],
                        status = task['status'],
                        createdAt = datetime.fromisoformat(task['createdAt']),
                        updatedAt = datetime.fromisoformat(task['updatedAt'])
                ))

    def handle(self, verb, arguments):
        if verb not in self.acceptable_verbs:
            print(f"Unacceptable verb: {verb}")
            print(f"Acceptable verbs: {self.acceptable_verbs}")
            return False
        if verb == 'add':
            task = Task(' '.join(arguments))
            self.tasks.append(task)
            print(f"Task added successfully (ID: {task.id})")
        return True

    def run(self):
        if len(sys.argv) == 1:
            sys.exit(1)
        verb, arguments = sys.argv[1], sys.argv[2:]
        if self.handle(verb, arguments):
            with open(self.file, 'w') as f:
                json.dump(self.tasks, f, cls=TaskEncoder, indent=4)


if __name__=="__main__":
    c = CommandLineHandler()
    c.run()
    