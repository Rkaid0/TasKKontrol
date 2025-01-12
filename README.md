<div align="center">
  <img src="https://raw.githubusercontent.com/Rkaid0/TasKKontrol/main/images/TasKKontrol_outline_small.png" alt="TasKKontrol Logo" width="400">
</div>

TasKKontrol is a package for automating tasks.

Basic structure:
- `Trigger` objects are used to keep track of when tasks need to execute.
- `Task` objects link together a `Trigger` object and a function that represents the task.
- A singular `Kontroller` object is used to manage all tasks.

## Triggers
This version of this package implements 3 types of triggers all inheriting the `Trigger` object.

### `ConditionTrigger` Object:
Defined using a function, which when returns `True` will activate the trigger.
Example usage:
```python
value = 10

def is_large ():
      global value
      return True if value > 5 else False

my_trigger = ConditionTrigger(is_large)
```

### `CompletionTrigger` Object:
Defined using another `Task` object, trigger activates when the task is finished executing.
Example usage:
```python
def true ():
      return True

def do_work ():
      print("Working")

first_task = Task(ConditionTrigger(true), do_work)
second_task = Task(CompletionTrigger(first_task), do_work)
```

### `TimerTrigger` Object:
Defined using a `gmtime` object, trigger will activate at the time of the object.
Example usage:
```python
from time import time, gmtime

start_time = time()

delay_trigger = TimerTrigger(gmtime(start_time + 10)) #10 second delay
```

## Tasks
### `Task` Object:
Constructor takes a `Trigger` object and a target function which will be executed when the trigger activates.
Example usage:
```python
value = 10

def is_large ():
      global value
      return True if value > 5 else False

def do_work ():
      print("Working")

my_task = Task(ConditionTrigger(is_large), do_work)
```

## Kontroller
### `Kontroller` Object:
All tasks need to be added to a `Kontroller` instance using the `addTask()` member function. To begin the execution of tasks the `Kontroller` instance needs to be started either with the `start()` or `launch()` member functions. Using the `start()` function is recomended as it initiates the `Kontroller` on a seperate thread allowing for concurrent execution.
Example usage:
```python
from TasKKontrol.Task import Task
from TasKKontrol.Triggers import ConditionTrigger, CompletionTrigger
from TasKKontrol.Kontroller import Kontroller

def true ():
      return True

def print1 ():
      print("1")

def print2 ():
      print("2")

def print3 ():
      print("3")

# instantiate Kontroller
kontroller = Kontroller()

# create tasks
task1 = Task(ConditionTrigger(true), print1)
task2 = Task(CompletionTrigger(task1), print2)
task3 = Task(CompletionTrigger(task2), print3)

# add tasks
kontroller.addTask(task1)
kontroller.addTask(task2)
kontroller.addTask(task3)

# start the kontroller
kontroller.start()

# start() function is nonblocking
print("Work in parallel with kontroller")

# wait for kontroller to finish
kontroller.wait_finish()
```

Created and maintained by Artyom Yesayan