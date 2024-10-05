from datetime import datetime
import json
import os
from my_tasks.task import Task
from my_tasks.task_encoder import TaskEncoder


class CommandLineHandler:

    def __init__(self, filename: str = 'tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self) -> list:
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

    def handle(self, verb: str, arguments: list):
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
        if verb == 'update':
            task_id, new_description = arguments
            for task in self.tasks:
                if task.id == task_id:
                    task.update_description(new_description)
                    self.save_tasks()
                    print(f"Task updated successfully (ID: {task.id})")
                    break
        if verb == 'delete':
            task_id = arguments[0]
            for task in self.tasks:
                if task.id == task_id:
                    self.tasks.remove(task)
                    self.save_tasks()
                    print(f"Task deleted successfully (ID: {task.id})")
                    break
