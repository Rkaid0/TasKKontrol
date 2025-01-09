from time import time, gmtime, struct_time

from Utils import same_time

class Trigger:
      def __init__ (self):
            self.createdTime = time()

      def should_be_active (self):
            return False

      def same (self, other):
            return False

class ConditionTrigger (Trigger):
      def __init__ (self, conditionFunction):
            super().__init__()
            self.conditionfunction = conditionFunction

      def should_be_active (self):
            if self.conditionfunction():
                  return self
            else:
                  return None
            
      def same (self, other):
            return self == other

class CompletionTrigger (Trigger):
      def __init__ (self, assosiatedTask):
            super().__init__()
            self.assosiatedTask = assosiatedTask

      def same (self, other):
            if not isinstance(other, CompletionTrigger):
                  return False
            
            return self.assosiatedTask == other.assosiatedTask

class TimerTrigger (Trigger):
      def __init__ (self, time):
            super().__init__()
            self.time = time

      def should_be_active (self):
            return same_time(self.time, gmtime())
      
      def same (self, other):
            if not isinstance(other, TimerTrigger):
                  return False
            
            return same_time(self.time, other.time)