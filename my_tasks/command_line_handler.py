from my_tasks.task import Task
from my_tasks.task_encoder import TaskEncoder
from datetime import datetime
import json
import os
import sys


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
