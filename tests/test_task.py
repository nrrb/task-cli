from datetime import datetime
import unittest
from my_tasks.task import Task


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test task")
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.status, "to-do")
        self.assertIsInstance(task.createdAt, datetime)

if __name__ == '__main__':
    unittest.main()
