import os
import tempfile

# File stored in a safe temporary directory
FILE_NAME = os.path.join(tempfile.gettempdir(), "tasks.txt")

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available!")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def run_commands(commands):
    """Run commands from a predefined list instead of input()"""
    tasks = load_tasks()

    for command in commands:
        action = command[0]

        if action == "view":
            show_tasks(tasks)

        elif action == "add":
            task_name = command[1]
            tasks.append(task_name)
            save_tasks(tasks)
            print(f"Task added: {task_name}")

        elif action == "exit":
            print("Exiting...")
            break

if __name__ == "__main__":
    print(f"Tasks file path: {FILE_NAME}\n")

    # Predefined commands simulating user input
    commands = [
        ("view",),
        ("add", "Buy groceries"),
        ("add", "Call doctor"),
        ("view",),
        ("exit",)
    ]

    run_commands(commands)
