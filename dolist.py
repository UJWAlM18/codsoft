def display_list(todo_list):
    print("To-Do List:")
    for index, task in enumerate(todo_list, 1):
        print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index.")
todo_list = []

add_task(todo_list, "Buy groceries")
add_task(todo_list, "Finish homework")
add_task(todo_list, "Go for a run")

display_list(todo_list)

remove_task(todo_list, 3)

display_list(todo_list)