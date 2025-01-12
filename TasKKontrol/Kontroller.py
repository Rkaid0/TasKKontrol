from threading import Thread, Lock
from time import sleep

from TasKKontrol.Triggers import CompletionTrigger
from TasKKontrol.Task import Status

class Kontroller:
      def __init__ (self, tasks=[], triggers=[]):
            self.dormant_triggers = triggers
            self.active_triggers = []
            self.tasks = tasks
            self.active_processes = {}
            self.wait_loop_limiter = 0.1
            self.satus = Status.DORMANT
            self.thread = None
            self.lock = Lock()

      def update_triggers (self):
            self.lock.acquire()

            index = 0
            while index < len(self.dormant_triggers):
                  trigger = self.dormant_triggers[index]

                  if trigger.should_be_active():
                        self.active_triggers.append(trigger)
                        self.dormant_triggers.pop(index) 
                  else:
                        index += 1

            self.lock.release()

      def launch (self) :
            self.status = Status.ACTIVE

            while self.dormant_tasks_exist():
                  self.update_triggers()

                  if len(self.active_triggers) > 0:
                        self.lock.acquire()

                        trigger = self.active_triggers.pop(0)

                        for i, task in enumerate(self.tasks):
                              if task.trigger.same(trigger):
                                    task = self.tasks[i]
                                    task.launch()
                                    self.active_triggers.append(CompletionTrigger(task))
                        
                        self.lock.release()

                  sleep(self.wait_loop_limiter)

            self.status = Status.SUCCESS

      def start (self):
            if self.thread and self.thread.is_alive():
                  return False
            
            self.thread = Thread(target=self.launch, daemon=True)
            self.thread.start()

      def wait_finish (self):
            if self.thread:
                  self.thread.join()

      def addTask (self, task):
            self.lock.acquire()
            self.tasks.append(task)
            self.dormant_triggers.append(task.trigger)
            self.lock.release()

      def addTrigger (self, trigger):
            self.lock.acquire()
            self.dormant_triggers.append(trigger)
            self.lock.release()

      def dormant_tasks_exist (self):
            for task in self.tasks:
                  if task.status == Status.DORMANT:
                        return True
                  
            return False

      def print_status (self):
            for task in self.tasks:
                  print(f"[{task.target.__name__}] : {task.status}")