import unittest
from unittest.mock import patch, mock_open
from my_tasks.command_line_handler import CommandLineHandler

class TestCommandLineHandler(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_initialization_creates_empty_file(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        mock_open_file.assert_any_call("tasks.json", "w")

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_handle_add(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        with patch("builtins.open") as mock_open:
            handler.handle("add", ["Buy milk"])
            self.assertEqual(len(handler.tasks), 1)
            self.assertEqual(handler.tasks[0].description, "Buy milk")
            mock_open.assert_called_with("tasks.json", "w")

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_handle_list(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        handler.handle("add", ["Buy milk"])
        handler.handle("add", ["Buy eggs"])
        handler.handle("add", ["Buy bread"])
        with patch("builtins.print") as mock_print:
            handler.handle("list", [])
            self.assertEqual(mock_print.call_count, 3)
            handler.handle("list", ["to-do"])
            self.assertEqual(mock_print.call_count, 6)
            handler.handle("list", ["in-progress"])
            # No change in the count since there are no tasks with status in-progress
            self.assertEqual(mock_print.call_count, 6) 

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_handle_update(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        handler.handle("add", ["Buy milk"])
        with patch("builtins.print") as mock_print:
            handler.handle("list", [])
            # Get the output from the mock_print and extract the Task ID
            task_id = mock_print.call_args[0][0].__str__().split(":")[0]
            handler.handle("update", [task_id, "Buy fruits"])
            self.assertEqual(handler.tasks[0].description, "Buy fruits")

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_handle_delete(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        handler.handle("add", ["Buy milk"])
        with patch("builtins.print") as mock_print:
            handler.handle("list", [])
            # Get the output from the mock_print and extract the Task ID
            task_id = mock_print.call_args[0][0].__str__().split(":")[0]
            handler.handle("delete", [task_id])
            self.assertEqual(len(handler.tasks), 0)

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_handle_mark_in_progress(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        handler.handle("add", ["Buy milk"])
        with patch("builtins.print") as mock_print:
            handler.handle("list", [])
            # Get the output from the mock_print and extract the Task ID
            task_id = mock_print.call_args[0][0].__str__().split(":")[0]
            handler.handle("mark-in-progress", [task_id])
            self.assertEqual(handler.tasks[0].status, "in-progress")

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_handle_mark_done(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        handler.handle("add", ["Buy milk"])
        with patch("builtins.print") as mock_print:
            handler.handle("list", [])
            # Get the output from the mock_print and extract the Task ID
            task_id = mock_print.call_args[0][0].__str__().split(":")[0]
            handler.handle("mark-done", [task_id])
            self.assertEqual(handler.tasks[0].status, "done")


if __name__ == '__main__':
    unittest.main()