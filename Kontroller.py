from Triggers import CompletionTrigger

class Kontroller:
      def __init__ (self, tasks=[], triggers=[]):
            self.pending_triggers = triggers
            self.active_triggers = []
            self.tasks = tasks

      def run (self):
            while len(self.tasks) > 0:
                  index = 0
                  while index < len(self.pending_triggers):
                        trigger = self.pending_triggers[index]

                        if trigger.should_be_active():
                              self.active_triggers.append(trigger)
                              self.pending_triggers.pop(index) 
                        else:
                              index += 1

                  if len(self.active_triggers) > 0:
                        trigger = self.active_triggers.pop(0)
                        
                        for i, task in enumerate(self.tasks):
                              if (task.trigger.same(trigger)):
                                    task.launch()
                                    self.tasks.pop(i)
                                    self.active_triggers.append(CompletionTrigger(task))

            print("No More Tasks Left")

      def addTask (self, task):
            self.tasks.append(task)
            self.pending_triggers.append(task.trigger)

      def addTrigger (self, trigger):
            self.pending_triggers.append(trigger)