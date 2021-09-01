tasks = [ 
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks


def find_uncompleted_task(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task) 
    return uncompleted_tasks
print(find_uncompleted_task(tasks))


# # Print a list of completed tasks


def find_completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

print(find_completed_tasks(tasks))


# # Print a list of all task descriptions


def task_description(list):
    description_task = []
    for task in list:
        description_task.append(task["description"])
    return description_task
print(task_description(tasks))


# # Print a list of tasks where time_taken is at least a given time


def time_to_complete_task(list, time):
    complete_the_task = []
    for task in list:
        if task["time_taken"] >= time:
            complete_the_task.append(task)
    return complete_the_task
print(time_to_complete_task(tasks, 30))


# Print any task with a given description

def task_described(list, parameter_description):
    described = []
    for task in list:
        if task["description"] == parameter_description:
            described.append(task)
    return described
print(task_described(tasks, "Feed Cat"))

