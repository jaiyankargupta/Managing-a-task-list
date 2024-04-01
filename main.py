class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            print(f"{idx}. {task.title} - {task.description} [{status}]")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
            print("Task added successfully.")
        elif choice == "2":
            title = input("Enter title of task to mark as completed: ")
            task_manager.complete_task(title)
        elif choice == "3":
            task_manager.display_tasks()
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
