#Startting the application:
# Function to display the menu and prompt the user for an action
def menu():
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Good Bye.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).\n")

# To-Do List Application

# Initialize an empty list to store tasks
to_do_list = []

# Function to add a task to the list

def add_task():
    while True:
        task = input("Enter the task: ").strip()
        if task:        # check if task is not empty
            to_do_list.append(task)
            print(f" '{task}' has been added to the list.\n")
            break
        else:
            print("Task cannot be empty. Please enter a valid task.\n")

# Function idea: Add more if not press N




# Function to remove a task from the list
def remove_task():
    while True:
        if not to_do_list:
            print("No tasks to remove.\n")
            return

        print("Current Tasks:")
        for idx, task in enumerate(to_do_list, start=1):
            print(f"{idx}. {task}")

        try:
            task_num = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_num < len(to_do_list):
                removed_task = to_do_list.pop(task_num)
                print(f"'{removed_task}' has been removed from the list.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid task.\n")



# Function to view all tasks in the list
def view_tasks():
    if not to_do_list:
        print("No tasks in the list.\n")
    else:
        print("To-Do List:\n------------------")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")
            print(f"\nTotal tasks: {len(to_do_list)}\n")

# Function idea: go back to Home Menu


# Run the to-do list application
if __name__ == "__main__":
    menu()









