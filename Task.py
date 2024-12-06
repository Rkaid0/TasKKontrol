class Task:
      def __init__ (self, trigger, target):
            self.trigger = trigger
            self.target = target

      def launch (self, argumets=None):
            if argumets:
                  self.target(argumets)
            else:
                  self.target()