import arrow

class Task:
    def __init__(self):
        completed = False
        priority = 0
        name = ""

    # integratedML stuff
    
    def boundaries():
        pass
        # some integratedML shit

    # user input stuff
    def newName(self):
        name = input("> ")
        print(name, "is the name of the task")

    def newTaskLength(self):
        print("Task length (hours): ")
        task_length = input("> ")
        print(task_length, "is the length of the task")
    
    def completed(self):
        completed = True

# test_task = Task()
# test_task.newName()