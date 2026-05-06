import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
def add_task_logic(tasks, task):
    now_time = datetime.now().strftime("%H:%M:%S")
    now_date = datetime.now().strftime("%Y-%m-%d")
    tasks.append(f"{now_date}\n{now_time}\n{task}")

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
            print(f"{i}. {task['date']}")
            print(f"   {task['time']}")
            print(f"   {task['task']}\n")

def add_task_logic(tasks, task):
    now = datetime.now()
    
    tasks.append({
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "task": task
    })

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
        now = datetime.now()
        current_time = now.strftime("\n%d-%m-%y \n%H:%M:%S")
        
        print("\n      TO-DO LIST     \n")
        
        print(f"Date & Time: {current_time}\n")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks(tasks)
            input("\nPress Enter to continue...")
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
            input("\nPress Enter to continue...")
        elif choice == "4":
            print("\nGoodbye, see you next time!\n")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()