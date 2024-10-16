#Startting the application:
# Function to display the menu and prompt the user for an action
from datetime import datetime
current_datetime = datetime.now()
f_date = current_datetime.strftime("%Y-%m-%d")  #formatted current date
priority_order = {"high": 1, "medium": 2, "low": 3}

# Initialize an empty list to store tasks
to_do_list = []


def menu():
    while True:
        print("Advanced To-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Suggest Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        print()

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            suggest_tasks()
        elif choice == '5':
            print("Exiting the application. Good Bye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).\n")

# To-Do List Application
#<<1>>
def add_task():
    while True:
        task = input("Enter the task: ").strip()

        if task.isdigit():
            print("Task cannot be numeric. Please enter a valid task.\n")
            continue

        if not task:
            print("Task cannot be empty. Please enter a valid task.\n")
            continue

        if task:
            while True:    # get priority
                priority = input("Enter the priority (high, medium, low): ").strip().lower()
                if priority in ['high', 'medium', 'low']:
                    break     # valid
                else:
                    print("Invalid priority. Please enter 'high', 'medium', or 'low'.\n")

            while True:     #get deadline
                deadline = input("Enter the deadline (YYYY-MM-DD): ").strip()

                try:
                    deadline = datetime.strptime(deadline, "%Y-%m-%d")
                    f_deadline = deadline.strftime("%Y-%m-%d")   #formatted deadline

                    if deadline >= current_datetime:
                        print(f"Deadline is {f_deadline}")
                        break

                    else:
                        print(f"Invalid deadline. The deadline {f_deadline} is before the current time {f_date}.")

                except ValueError:
                    print("Invalid date format. Please enter YYYY-MM-DD")

            to_do_list.append({"task": task, "priority": priority, "deadline": f_deadline})
            print(f"'{task}' with priority '{priority}' and deadline '{f_deadline}' has been added to the list.\n")
            break



# Function idea: Add more if not press N




# Function to remove a task from the list
#<<2>>
def remove_task():
    while True:
        if not to_do_list:
            print("No tasks to remove.\n")
            return

        print("Current To-Do List:")
        for idx, k in enumerate(to_do_list, 1):
            print(f"{idx}. {k["task"]} - {k["priority"]} - {k["deadline"]}")
        print()

        try:
            removed_task = input("Enter the task to remove: ").strip()

            ##### 'enter' malfunctioning

            for k in to_do_list:
                if k["task"].lower() == removed_task.lower():   # case insensitive
                    to_do_list.remove(k)
                    print(f"'{removed_task}' has been removed from the list")
                    break

            else:
                print("Task not found in the list. Please enter a valid task\n")

        except ValueError:
            print("Please enter a valid task.\n")



##### function idea: no more to remove


# Function to view all tasks in the list
# <<3>>
def view_tasks():
    if not to_do_list:
        print("No tasks in the list.\n")
    else:
        print("To-Do List:")
        for idx, k in enumerate(to_do_list, 1):
            print(f"{idx}. {k["task"]} - {k["priority"]} - {k["deadline"]}")

        print(f"\nTotal tasks: {len(to_do_list)}\n")

# Function idea: go back to Home Menu


# Function to suggest tasks
# <<4>>

def suggest_tasks():
    print("Good afternoon! Here are some tasks you might want to work on: ")

    # Sort tasks based on priority and deadline
    sorted_tasks = sorted(
        to_do_list,
        key=lambda x: (priority_order[x["priority"]], datetime.strptime(x["deadline"], "%Y-%m-%d"))
    )
        
    for idx, k in enumerate(sorted_tasks, 1):
        print(f"{idx}. {k["task"]} - {k["priority"]} - {k["deadline"]}")
    print()
# Run the to-do list application
if __name__ == "__main__":
    menu()









