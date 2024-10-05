# task-cli

MANAGE ALL THE TASKS!! 📑

Using [this great project idea starter](https://roadmap.sh/projects/task-tracker) on [roadmap.sh](https://roadmap.sh), this is a fun and simple Python script that you could make with the skills you'd learn from a Python beginner tutorial. 

Run it in the browser for free with Replit:

[![Run on Replit](https://replit.com/badge/github/nrrb/task-cli)](https://replit.com/github/nrrb/task-cli)


## How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/nrrb/number-guessing-game.git
```

2. From a command line where Python is available, change directory to the repo and run:

```bash
python task-cli.py
```

### Add a Task

```bash
python task-cli.py add "Water the roses."
```

### List Tasks

You can list all tasks:

```bash
python task-cli.add list
```

Or you can list tasks by status (to-do, in-progress, or done):

```bash
python task-cli.py list to-do
```

### Update a Task

Given the unique ID for a task that's already been added (you get this when you add a task or list tasks), you can change the description for that task.

```bash
python task-cli.py update e641c "Take vitamins."
```

### Delete a Task

Given the unique ID for a task that's already been added (you get this when you add a task or list tasks), you can delete that task.

```bash
python task-cli.py delete e641c
```

## Running Tests

Run:

```bash
python3 -m unittest discover tests
```
