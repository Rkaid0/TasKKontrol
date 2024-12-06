from Task import Task
from Triggers import ConditionTrigger, TimeTrigger, CompletionTrigger
from Kontroller import Kontroller

from time import time, gmtime

x = 0

def func ():
      global x
      x += 1
      print("X is " + str(x))

start_time = time()

kontroller = Kontroller()

task1 = Task(TimeTrigger(gmtime(time()+1)), func)
task2 = Task(TimeTrigger(gmtime(time()+2)), func)
task3 = Task(TimeTrigger(gmtime(time()+3)), func)
task4 = Task(TimeTrigger(gmtime(time()+4)), func)
task5 = Task(ConditionTrigger(lambda: x >= 2), lambda: print("X is more than or equal to 2"))
task6 = Task(CompletionTrigger(task4), lambda: print("end"))

kontroller.addTask(task1)
kontroller.addTask(task2)
kontroller.addTask(task3)
kontroller.addTask(task4)
kontroller.addTask(task5)
kontroller.addTask(task6)

kontroller.run()