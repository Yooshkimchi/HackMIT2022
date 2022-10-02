import arrow
from queue import PriorityQueue

class Task(object):
    def __init__(self):
        self.completed = False
        self.priority = 0
        self.task_name = ""

    # integratedML stuff
    
    def getStartTime(self, time):
        converted_time = str(time / 60) + ":" + str(time % 60) + ":00"
        return converted_time

    # user input stuff
    def newName(self, new_name):
        self.task_name = new_name

    def getName(self):
        return self.task_name

    def newPriority(self, priority):
        self.priority = priority

    def getPriority(self):
        return self.priority

    def newTaskLength(self, length):
        task_length = length
    
    def completed(self):
        self.completed = True


def isolate_priorities(e):
    return e.getPriority()

# inputs taskList as a dictionary (key = task priority, value = object)
def priority_manager(taskList):
    print(taskList)
    taskList.sort(key=isolate_priorities)
    return taskList

# def time_manager(taskList):


taskList = []

tTask = Task()
tTask.newName("fuck me")
tTask.newPriority(2)
print(tTask.getStartTime(240))
taskList.append(tTask)

tTask2 = Task()
tTask2.newName("test 2")
tTask2.newPriority(6)
taskList.append(tTask2)

tTask3 = Task()
tTask3.newName("fuck test 4")
tTask3.newPriority(2)
taskList.append(tTask3)

plist = priority_manager(taskList)

for task in plist:
    print(task.getName())