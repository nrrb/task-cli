import json
import unittest
from my_tasks.task import Task
from my_tasks.task_encoder import TaskEncoder

class TestTaskEncoder(unittest.TestCase):
    def test_task_serialization(self):
        task = Task("Test task", id="abcde")
        task_json = json.dumps(task, cls=TaskEncoder)
        self.assertIn('"description": "Test task"', task_json)
