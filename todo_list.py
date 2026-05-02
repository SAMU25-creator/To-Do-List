import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
        
def add_task_logic(tasks, task):
    tasks.append(task)

def remove_task_logic(tasks, index):
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    return None     
        

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    add_task_logic(tasks, task)
    save_tasks(tasks)
    print("Task added!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        removed = remove_task_logic(tasks, task_num)
        if removed is not None:
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n      TO-DO LIST     \n")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\nGoodbye, see you next time!\n")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()