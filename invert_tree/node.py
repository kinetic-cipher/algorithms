
class Node:

    def __init__(self,val):
       self.val = val
       self.left = None
       self.right = None

    def print_all(self):
        print(self.val)
        if self.left != None:
           self.left.print_all()
        if self.right != None:
           self.right.print_all()
    
     
