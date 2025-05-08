def add_task(task_list, task_name, task_due):
    task = {'name': task_name, 'due': task_due, 'complete': False}
    task_list.append(task)

def delete_task(task_list, task_name):
    return [task for task in task_list if task['name'] != task_name]

def display_tasks(task_list):
    print("All Tasks:")
    for task in task_list:
        print(f"Task: {task['name']}, Due: {task['due']}, Completed: {task['complete']}")

def complete_task(task_list, task_name):
    for i in range(len(task_list)):
        if task_list[i]['name'] == task_name:
            task_list[i]['complete'] = True
            return
    print("Task not found.")

task_list = []

add_task(task_list, "Fix bug in code", "2024-02-21")
add_task(task_list, "Update documentation", "2024-02-22")
display_tasks(task_list)
complete_task(task_list, "Fix bug in code")
task_list = delete_task(task_list, "Update documentation")  
display_tasks(task_list)