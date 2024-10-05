from datetime import datetime
import json
import os
from my_tasks.task import Task
from my_tasks.task_encoder import TaskEncoder


class CommandLineHandler:

    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)
        with open(self.filename, 'r') as f:
            tasks = json.load(f)
            return [
                Task(
                        description = task['description'],
                        id = task['id'],
                        status = task['status'],
                        createdAt = datetime.fromisoformat(task['createdAt']),
                        updatedAt = datetime.fromisoformat(task['updatedAt'])
                )
                for task in tasks
            ]

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, cls=TaskEncoder, indent=4)

    def handle(self, verb, arguments):
        if verb == 'add':
            task = Task(' '.join(arguments))
            self.tasks.append(task)
            self.save_tasks()
            print(f"Task added successfully (ID: {task.id})")
        if verb == 'list':
            if len(arguments) == 0:
                for task in self.tasks:
                    print(task)
            elif arguments[0] in ['to-do', 'done', 'in-progress']:
                status = arguments[0]
                for task in self.tasks:
                    if task.status == status:
                        print(task)
