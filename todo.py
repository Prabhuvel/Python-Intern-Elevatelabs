class Todolist:
    def __init__(self, choice):
        self.choice = choice
        if self.choice == 1:
            self.add_task()
        elif self.choice == 2:
            self.view_tasks()
        elif self.choice == 3:
            self.remove_task()
        else:
            print("Invalid choice!")

    def add_task(self):
        with open("tasks.txt", "a") as file:  # append so we don't overwrite
            task = input("Enter your task: ")
            file.write(task + "\n")
        print("Task added successfully!")

    def view_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks found!")
        except FileNotFoundError:
            print("No task file found! Add some tasks first.")

    def remove_task(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            if not tasks:
                print("No tasks to remove!")
                return

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

            choice = int(input("Enter the task number to remove: "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Removed task: {removed.strip()}")
            else:
                print("Invalid task number!")
        except FileNotFoundError:
            print("No task file found! Add some tasks first.")


# Menu
print("Welcome to To-Do List")
print("1. Write your tasks")
print("2. View your tasks")
print("3. Remove a task")

try:
    choice = int(input("Enter your choice: "))
    Todolist(choice)
except ValueError:
    print("Please enter a valid number!")
