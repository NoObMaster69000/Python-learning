import os

# Define the filename for storing tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """
    Loads tasks from the tasks.txt file.
    If the file doesn't exist, it returns an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        # Read lines, and strip newline characters from each task
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    """
    Saves the current list of tasks to the tasks.txt file.
    Each task is written on a new line.
    """
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\\n")

def show_tasks(tasks):
    """
    Displays the list of tasks to the user.
    """
    print("\\n--- To-Do List ---")
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("--------------------\\n")

def add_task(tasks):
    """
    Prompts the user to add a new task and adds it to the list.
    """
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")
    save_tasks(tasks)

def remove_task(tasks):
    """
    Prompts the user to remove a task by its number.
    Handles invalid input and out-of-range numbers.
    """
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed successfully.")
            save_tasks(tasks)
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """
    The main function that runs the to-do list application loop.
    """
    tasks = load_tasks()

    while True:
        print("What would you like to do?")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
