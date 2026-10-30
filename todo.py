
tasks = []

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add a task
    if choice == "1":
        task_title = input("Enter your task: ")

        if task_title.strip():
            tasks.append({
                "title": task_title,
                "completed": False
            })
            print("Task added successfully!")
        else:
            print("Task cannot be empty!")

    # View all tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available!")
        else:
            print("\n===== YOUR TASKS =====")

            for index, task in enumerate(tasks, start=1):
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{index}. {task['title']} - {status}")

    # Delete a task
    elif choice == "3":
        if not tasks:
            print("No tasks to delete!")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")

            try:
                task_number = int(
                    input("Enter task number to delete: ")
                )

                if 1 <= task_number <= len(tasks):
                    deleted_task = tasks.pop(task_number - 1)
                    print(f"Deleted: {deleted_task['title']}")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    # Mark a task as completed
    elif choice == "4":
        if not tasks:
            print("No tasks available!")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")

            try:
                task_number = int(
                    input("Enter task number to complete: ")
                )

                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    # Exit the program
    elif choice == "5":
        print("Goodbye! Keep learning Python!")
        break

    else:
        print("Invalid choice. Please select 1-5.")
