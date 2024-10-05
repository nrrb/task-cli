from datetime import datetime
import time
import unittest
from my_tasks.task import Task


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test task")
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.status, "to-do")
        self.assertIsInstance(task.createdAt, datetime)

    def test_task_update_description(self):
        task = Task("Test task")
        old_updated_at = task.updatedAt
        time.sleep(0.1)
        task.update_description("Updated task")
        new_updated_at = task.updatedAt
        self.assertEqual(task.description, "Updated task")
        self.assertGreater(new_updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
