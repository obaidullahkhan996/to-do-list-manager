import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"
tasks = []


# Load saved tasks
def load_tasks():
    global tasks

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, OSError):
            tasks = []


# Save tasks to a file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Display tasks in the window
def refresh_tasks():
    task_list.delete(0, tk.END)

    for index, task in enumerate(tasks):
        if task["completed"]:
            status = "✓ Completed"
        else:
            status = "○ Pending"

        task_list.insert(
            tk.END,
            f"{index + 1}. {task['title']} - {status}"
        )


# Add a new task
def add_task():
    title = task_entry.get().strip()

    if not title:
        messagebox.showwarning(
            "Empty Task",
            "Please enter a task first!"
        )
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks()
    refresh_tasks()
    task_entry.delete(0, tk.END)


# Mark a task as completed
def complete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a task first!"
        )
        return

    index = selected[0]
    tasks[index]["completed"] = True

    save_tasks()
    refresh_tasks()


# Delete a task
def delete_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a task to delete!"
        )
        return

    index = selected[0]
    deleted_task = tasks.pop(index)

    save_tasks()
    refresh_tasks()

    messagebox.showinfo(
        "Task Deleted",
        f"Deleted: {deleted_task['title']}"
    )


# Create the main window
root = tk.Tk()
root.title("My To-Do List Manager")
root.geometry("550x500")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

# Heading
heading = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 24, "bold"),
    bg="#f0f4f8",
    fg="#1e3a5f"
)
heading.pack(pady=20)

# Task input
task_entry = tk.Entry(
    root,
    font=("Arial", 13),
    width=35
)
task_entry.pack(pady=5)

# Add button
add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task,
    width=18,
    bg="#2563eb",
    fg="white",
    font=("Arial", 11, "bold")
)
add_button.pack(pady=8)

# Task list
task_list = tk.Listbox(
    root,
    width=55,
    height=12,
    font=("Arial", 11),
    selectmode=tk.SINGLE
)
task_list.pack(pady=10)

# Button area
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=10)

complete_button = tk.Button(
    button_frame,
    text="Complete",
    command=complete_task,
    width=12,
    bg="#16a34a",
    fg="white"
)
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    command=delete_task,
    width=12,
    bg="#dc2626",
    fg="white"
)
delete_button.grid(row=0, column=1, padx=5)

# Start the application
load_tasks()
refresh_tasks()

root.mainloop()