import json
import os

FILE_NAME = "List.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def pause():
    input("\nPress Enter to return to the menu...")

def main():
    tasks = load_tasks()

    while True:
        print("\n                TO-DO LIST                 ")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit\n")

        choice = input("Choose an option: \n")

        if choice == "1":
            show_tasks(tasks)
            pause()
        elif choice == "2":
            add_task(tasks)
            pause()
        elif choice == "3":
            remove_task(tasks)
            pause()
        elif choice == "4":
            print("Goodbye, see you next time!")
            pause()
            break
        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()