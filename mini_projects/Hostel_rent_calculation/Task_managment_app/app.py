def task():
    tasks = []  # Initialize an empty list to store tasks
    print("---- WELCOME TO THE TASK MANAGEMENT APP ----")
    
    # Add initial tasks
    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        while True:
            task_name = input(f"Enter task {i}: ").strip()
            if task_name:  # Ensure task is not empty
                tasks.append(task_name)
                break
            else:
                print("Task cannot be empty. Please try again.")
    
    print(f"Today's tasks are:\n{tasks}")
    
    while True:
        try:
            print("\nOptions:")
            print("1 - Add Task")
            print("2 - Update Task")
            print("3 - Delete Task")
            print("4 - View Tasks")
            print("5 - Exit")
            operation = int(input("Enter your choice (1-5): "))
            
            if operation == 1:  # Add Task
                while True:
                    add = input("Enter the task you want to add: ").strip()
                    if add:  # Ensure task is not empty
                        tasks.append(add)
                        print(f"Task '{add}' has been successfully added.")
                        break
                    else:
                        print("Task cannot be empty. Please try again.")
            
            elif operation == 2:  # Update Task
                updated_val = input("Enter the task name you want to update: ").strip()
                if updated_val in tasks:
                    while True:
                        up = input("Enter the new task: ").strip()
                        if up:  # Ensure updated task is not empty
                            ind = tasks.index(updated_val)
                            tasks[ind] = up
                            print(f"Updated task '{updated_val}' to '{up}'.")
                            break
                        else:
                            print("Task cannot be empty. Please try again.")
                else:
                    print("Task not found.")
            
            elif operation == 3:  # Delete Task
                del_val = input("Enter the task you want to delete: ").strip()
                if del_val in tasks:
                    tasks.remove(del_val)
                    print(f"Task '{del_val}' has been deleted.")
                else:
                    print("Task not found.")
            
            elif operation == 4:  # View Tasks
                if tasks:
                    print("Your tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                else:
                    print("No tasks available.")
            
            elif operation == 5:  # Exit
                print("Closing the program....")
                break
            
            else:
                print("Invalid input. Please enter a number from 1 to 5.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Run the task management app
task()