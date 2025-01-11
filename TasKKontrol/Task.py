from enum import Enum

class Task:
      def __init__ (self, trigger, target):
            self.trigger = trigger
            self.target = target
            self.status = Status.DORMANT

      def launch (self, argumets=None):
            try:
                  self.status = Status.ACTIVE

                  if argumets:
                        self.target(argumets)
                  else:
                        self.target()

                  self.status = Status.SUCCESS

            except:
                  print("Task [" + str(self) + "] failed")
                  self.status = Status.FAIL

class Status(Enum):
      DORMANT = 0
      ACTIVE = 1
      SUCCESS = 2
      FAIL = 3