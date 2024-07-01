class ToDoApp:
    def __init__(self):
        self.todos = []

    def add_todo(self, task):
        self.todos.append({"task": task, "completed": False})
        print(f"Added to-do: '{task}'")

    def delete_todo(self, index):
        try:
            removed_task = self.todos.pop(index)
            print(f"Deleted to-do: '{removed_task['task']}'")
        except IndexError:
            print("Error: To-do index out of range")

    def update_todo(self, index, new_task):
        try:
            self.todos[index]["task"] = new_task
            print(f"Updated to-do at index {index} to '{new_task}'")
        except IndexError:
            print("Error: To-do index out of range")

    def mark_as_completed(self, index):
        try:
            self.todos[index]["completed"] = True
            print(f"Marked to-do at index {index} as completed")
        except IndexError:
            print("Error: To-do index out of range")

    def show_todos(self):
        if not self.todos:
            print("No to-dos")
        for i, todo in enumerate(self.todos):
            status = "Completed" if todo["completed"] else "Not Completed"
            print(f"{i}: {todo['task']} - {status}")

def main():
    todo_app = ToDoApp()

    while True:
        print("\nTo-Do Application")
        print("1. Add To-Do")
        print("2. Delete To-Do")
        print("3. Update To-Do")
        print("4. Mark To-Do as Completed")
        print("5. Show All To-Dos")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_app.add_todo(task)
        elif choice == '2':
            index = int(input("Enter the index of the to-do to delete: "))
            todo_app.delete_todo(index)
        elif choice == '3':
            index = int(input("Enter the index of the to-do to update: "))
            new_task = input("Enter the new task: ")
            todo_app.update_todo(index, new_task)
        elif choice == '4':
            index = int(input("Enter the index of the to-do to mark as completed: "))
            todo_app.mark_as_completed(index)
        elif choice == '5':
            todo_app.show_todos()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
