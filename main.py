from Task import Task
from Triggers import ConditionTrigger, TimeTrigger, CompletionTrigger
from TaskManager import TaskManager

from time import time, gmtime

x = 0

def func ():
      global x
      x += 1
      print("X is " + str(x))

start_time = time()

taskManager = TaskManager()

task1 = Task(TimeTrigger(gmtime(time()+1)), func)
task2 = Task(TimeTrigger(gmtime(time()+2)), func)
task3 = Task(TimeTrigger(gmtime(time()+3)), func)
task4 = Task(TimeTrigger(gmtime(time()+4)), func)
task5 = Task(ConditionTrigger(lambda: x >= 2), lambda: print("X is more than or equal to 2"))
task6 = Task(CompletionTrigger(task4), lambda: print("end"))

taskManager.addTask(task1)
taskManager.addTask(task2)
taskManager.addTask(task3)
taskManager.addTask(task4)
taskManager.addTask(task5)
taskManager.addTask(task6)

taskManager.run()