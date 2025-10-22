# To-Do List App by Mehrab Hussain

FILE_NAME = "tasks.txt"

# read tasks from file
def read_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

# write tasks to file
def write_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# main program
while True:
    print("\n📋 To-Do List App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    tasks = read_tasks()

    if choice == "1":
        if not tasks:
            print("No tasks found 😴")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        write_tasks(tasks)
        print(f"✅ '{new_task}' added!")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = f"{tasks[num - 1]} (done)"
            write_tasks(tasks)
            print("👏 Task marked as done!")
        else:
            print("Invalid number!")

    elif choice == "4":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            write_tasks(tasks)
            print(f"🗑 '{removed}' deleted!")
        else:
            print("Invalid number!")

    elif choice == "5":
        print("👋 Exiting... Have a productive day!")
        break

    else:
        print("❌ Invalid choice! Try again.")