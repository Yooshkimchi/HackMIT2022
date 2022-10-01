import arrow
from queue import PriorityQueue

class Task(object):
    def __init__(self):
        self.completed = False
        self.priority = 0
        self.task_name = ""

    # integratedML stuff
    
    def boundaries():
        pass
        # some integratedML shit

    # user input stuff
    def newName(self, new_name):
        self.task_name = new_name
        print(self.task_name, "is the name of the task")

    def getName(self):
        return self.task_name

    def newPriority(self, priority):
        self.priority = priority

    def getPriority(self):
        return self.priority

    def newTaskLength(self):
        print("Task length (hours): ")
        task_length = input("> ")
        print(task_length, "is the length of the task")
    
    def completed(self):
        self.completed = True