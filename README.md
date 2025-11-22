# Task CLI 📝

This project is a solution to the [Task Tracker](https://roadmap.sh/projects/task-tracker) challenge on roadmap.sh.

A simple, robust, and persistent command-line interface (CLI) task manager written in Python. This tool allows you to manage your daily tasks, track their status, and save them locally without needing a database server.

## ✨ Features

- **Create Tasks:** Add new tasks quickly.
- **Read/List:** View all tasks or filter by status (`todo`, `in-progress`, `done`).
- **Update:** Modify existing task descriptions.
- **Delete:** Remove tasks permanently.
- **Status Tracking:** specific commands to mark tasks as "in-progress" or "done".
- **Persistent Storage:** Automatically saves all data to `data.json` so you never lose your tasks.
- **Table Formatting:** Displays tasks in a clean, readable table with text wrapping for long descriptions.

## 🛠️ Prerequisites

- **Python 3.6** or higher.
- No external libraries required! (Uses standard `json`, `os`, `datetime`, etc.)

## 🚀 How to Run

1. Save your Python code as `task_cli.py` (or any name you prefer).
2. Open your terminal or command prompt.
3. Run the script:

Bash

```
python task_cli.py
```

4. The prompt `task-cli >` will appear, waiting for your commands.

## 📖 Usage Guide

Here are the supported commands you can type into the CLI:

### 1. Add a Task

Add a new task to your list.

> **Tip:** Use quotes if your task has spaces.

Plaintext

```
add "Buy groceries for the week"
add "Finish Python project"
```

### 2. List Tasks

View your tasks in a table format. You can view all tasks or filter them.

Plaintext

```
list                  # Shows all tasks
list todo             # Shows only tasks that are To Do
list in-progress      # Shows only tasks In Progress
list done             # Shows only Completed tasks
```

### 3. Update a Task

Change the description of a task. You need the **ID** from the list command. _Syntax:_ `update <id> "New Description"`

Plaintext

```
update 1 "Buy groceries and snacks"
```

### 4. Change Status

Mark tasks as started or finished.

Plaintext

```
mark-in-progress 1    # Sets status to 'in-progress'
mark-done 1           # Sets status to 'done'
```

### 5. Delete a Task

Permanently remove a task.

Plaintext

```
delete 1
```

### 6. Exit

Close the application.

Plaintext

```
exit
```

## 📂 Project Structure

Plaintext

```
.
├── task_cli.py    # The main application logic
├── data.json      # Automatically created file where tasks are stored
└── README.md      # This documentation
```

## 🐛 Troubleshooting

- **"Error: Missing closing quote":** This usually happens if you typed `add "Task` but forgot the closing `"` at the end.
- **"Error: file not found":** If `data.json` doesn't exist yet, the program will create it automatically when you add your first task.
- **Windows/WSL Issues:** If you are using WSL and get file errors, ensure you are running the script inside the WSL terminal, not PowerShell.
