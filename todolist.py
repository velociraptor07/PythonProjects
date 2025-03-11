class Task:
    def __init__(self, title, description, priority="Medium"):
        self.title = title
        self.description = description
        self.completed = False
        self.priority = priority

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.title}\nDescription: {self.description}\nPriority: {self.priority}\nStatus: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added!")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed!")
                return
        print(f"Task '{title}' not found!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list!")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"\nTask {i}:\n{task}")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Task '{title}' marked as completed!")
                return
        print(f"Task '{title}' not found!")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Show All Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            priority = input("Enter task priority (Low/Medium/High): ").capitalize()
            task = Task(title, description, priority)
            todo_list.add_task(task)
        elif choice == "2":
            title = input("Enter the title of the task to remove: ")
            todo_list.remove_task(title)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            title = input("Enter the title of the task to mark as completed: ")
            todo_list.mark_task_completed(title)
        elif choice == "5":
            print("Exiting the To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
