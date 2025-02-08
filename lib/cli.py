from lib.models import session, Task

def add_task():
    """Function to add a new task."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    urgency = int(input("Enter urgency (1-5): "))
    importance = int(input("Enter importance (1-5): "))

    new_task = Task(title=title, description=description, urgency=urgency, importance=importance)
    session.add(new_task)
    session.commit()
    print( f"Task '{title}' added successfully!\n")


def view_tasks():
    """Function to display all tasks."""
    tasks = session.query(Task).all()
    
    if not tasks:
        print("No tasks found.\n")
        return
    
    print("\nTask List:")
    for task in tasks:
        print(f"ID: {task.id} | Title: {task.title} | Priority Score: {task.priority_score}")
    print()


def delete_task():
    """Function to delete a task by ID."""
    task_id = input("Enter the ID of the task to delete: ")
    task = session.query(Task).filter_by(id=task_id).first()

    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.title}' deleted successfully!\n")
    else:
        print("Task not found.\n")


def main():
    """CLI Menu for Task Prioritizer."""
    while True:
        print("\nTask Prioritizer CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
