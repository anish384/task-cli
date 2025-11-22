import json
import shlex
import textwrap
import os
from datetime import datetime

FILE_NAME = "data.json"


def load_tasks():
    """Reads the JSON file and returns a list of tasks."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Writes the list of tasks back to the JSON file."""
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")


def list_tasks(filter_status=None):
    tasks = load_tasks()
    
    if filter_status:
        tasks = [t for t in tasks if t.get("status", "todo") == filter_status]

    if not tasks:
        print(f"No tasks found{f' with status: {filter_status}' if filter_status else ''}.")
        return

    # Table Configuration
    ID_W, TASK_W, STAT_W, TIME_W = 5, 30, 15, 20
    header = f"{'ID':<{ID_W}} {'Task':<{TASK_W}} {'Status':<{STAT_W}} {'Created':<{TIME_W}}"
    
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for t in tasks:
        t_id = str(t.get("id", 0))
        t_task = t.get("task", "")
        t_status = t.get("status", "todo")
        t_time = t.get("created-on", "")[:19]

        wrapped_lines = textwrap.wrap(t_task, width=TASK_W) or [""]

        print(f"{t_id:<{ID_W}} {wrapped_lines[0]:<{TASK_W}} {t_status:<{STAT_W}} {t_time:<{TIME_W}}")

        for line in wrapped_lines[1:]:
            print(f"{'':<{ID_W}} {line:<{TASK_W}} {'':<{STAT_W}} {'':<{TIME_W}}")

    print("-" * len(header))

def add_task(args):
    if not args:
        print('Error: Use format -> add "Your task here"')
        return

    tasks = load_tasks()
    
    new_id = 1
    if tasks:
        new_id = max(t["id"] for t in tasks) + 1

    task_content = " ".join(args).strip('"')

    new_data = {
        "id": new_id,
        "task": task_content,
        "status": "todo",
        "created-on": datetime.now().isoformat(),
        "updated-on": datetime.now().isoformat()
    }

    tasks.append(new_data)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(args):
    if len(args) < 2 or not args[0].isdigit():
        print('Error: Use format -> update <id> "New Task Name"')
        return

    target_id = int(args[0])
    new_name = args[1]
    
    tasks = load_tasks()
    found = False
    
    for t in tasks:
        if t["id"] == target_id:
            t["task"] = new_name
            t["updated-on"] = datetime.now().isoformat()
            found = True
            break
    
    if found:
        save_tasks(tasks)
        print(f"Task {target_id} updated.")
    else:
        print(f"Task {target_id} not found.")

def delete_task(args):
    if not args or not args[0].isdigit():
        print("Error: Use format -> delete <id>")
        return

    target_id = int(args[0])
    tasks = load_tasks()
    
    # Filter out the task to delete
    initial_count = len(tasks)
    tasks = [t for t in tasks if t["id"] != target_id]
    
    if len(tasks) < initial_count:
        save_tasks(tasks)
        print(f"Task {target_id} deleted.")
    else:
        print(f"Task {target_id} not found.")

def change_status(args, status):
    if not args or not args[0].isdigit():
        print(f"Error: Use format -> mark-{status} <id>")
        return

    target_id = int(args[0])
    tasks = load_tasks()
    found = False

    for t in tasks:
        if t["id"] == target_id:
            t["status"] = status
            t["updated-on"] = datetime.now().isoformat()
            found = True
            break

    if found:
        save_tasks(tasks)
        print(f"Task {target_id} marked as {status}.")
    else:
        print(f"Task {target_id} not found.")


def main():
    print("""
    # Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
    """)
    
    while True:
        try:
            user_input = input("\ntask-cli > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if not user_input:
            continue

        if user_input == "exit":
            break

        # Use shlex to handle quotes automatically for ALL commands
        try:
            parts = shlex.split(user_input)
        except ValueError:
            print("Error: Missing closing quote.")
            continue

        command = parts[0].lower()
        args = parts[1:]

        if command == "add":
            add_task(args)
        elif command == "update":
            update_task(args)
        elif command == "delete":
            delete_task(args)
        elif command == "mark-in-progress":
            change_status(args, "in-progress")
        elif command == "mark-done":
            change_status(args, "done")
        elif command == "list":
            # Handle sub-commands for list
            if args and args[0] in ["done", "todo", "in-progress"]:
                list_tasks(args[0])
            else:
                list_tasks()
        else:
            print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
