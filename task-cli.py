#!/bin/python3
from my_tasks.command_line_handler import CommandLineHandler
import sys

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage: task-cli.py <verb> <arguments>")
        sys.exit(1)
    
    handler = CommandLineHandler()
    verb, arguments = sys.argv[1], sys.argv[2:]
    handler.handle(verb, arguments)
    