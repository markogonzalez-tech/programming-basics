tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

while True:
    print("\n--- TASK MANAGER ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
