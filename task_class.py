import arrow
from queue import PriorityQueue

class Task(object):
    def __init__(self):
        self.completed = False
        self.priority = 0
        self.task_name = ""

    # integratedML stuff

    def figureOutZeroes(self, time):
        if (time % 60 == 0):
            return "00"
        else:
            return str(time % 60)
    
    def getStartTime(self, time):
        a = arrow.utcnow()
        if (time < 600):
            converted_time = "0" + str(int(time / 60)) + ":" + self.figureOutZeroes(time) + ":00"
        else:
            converted_time = str(int(time / 60)) + ":" + self.figureOutZeroes(time) + ":00"
        converted_time = str(a.date()) + " " + converted_time
        datetime = arrow.get(converted_time, "YYYY-MM-DD HH:mm:ss")
        return datetime

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
print(tTask.getStartTime(800))
taskList.append(tTask2)

tTask3 = Task()
tTask3.newName("fuck test 4")
tTask3.newPriority(2)
taskList.append(tTask3)

plist = priority_manager(taskList)

for task in plist:
    print(task.getName())