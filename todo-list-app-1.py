#Objective:------------------------------------------------------------------------------------------
#Create a simple to-do list application that allows users to add, remove, and viewtasks
#This project will help you practice working with lists and functions in Python.

#Description:----------------------------------------------------------------------------------------
#In this project, you'll develop a console-based to-do list application. The
#application will provide a menu for the user to perform the following actions:
#1. Add a task to the to-do list.
#2. Remove a task from the to-do list.
#3. View all tasks in the to-do list.
#4. Exit the application.

#Features:-------------------------------------------------------------------------------------------
#1. Add Task: Allows the user to add a new task to the list.
#2. Remove Task: Allows the user to remove a task from the list.
#3. View Tasks: Displays all the tasks in the list.
#4. Exit: Ends the program.

#Startting the application:
# Function to display the menu and prompt the user for an action
def menu():
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

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
    task = input("Enter the task number: ")
    to_do_list.append(task)
    print(f" '{task}' has been added to the list.\n")
# Function to remove a task from the list
def remove_task():
    if not to_do_list:
        print("No tasks to remove.\n")
        return
    try:
        task_num = int(input("Enter the task to remove: ")) - 1
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
        print("To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")
        print()




# Run the to-do list application
if __name__ == "__main__":
    menu()




