
class Stack:

   def __init__(self):
      self.list = list()

   def push(self,value):
      self.list.append(value)

   def pop(self):
      return self.list.pop()         

   def print_all(self):
      print(self.list)
