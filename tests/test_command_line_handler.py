import unittest
from unittest.mock import patch, mock_open
from my_tasks.command_line_handler import CommandLineHandler

class TestCommandLineHandler(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.exists", return_value=False)
    def test_initialization_creates_empty_file(self, mock_exists, mock_open_file):
        handler = CommandLineHandler()
        mock_open_file.assert_any_call("tasks.json", "w")
