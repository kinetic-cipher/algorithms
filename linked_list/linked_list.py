import list_node as ln

class LinkedList:

   # initialize
   def __init__(self):
       self.head = None
       self.tail = None

   # insert(): insert at the tail
   def insert(self,value):
        new_node = ln.ListNode(value)
        new_node.next = None
        if self.head == None and self.tail == None:
           self.head = new_node
           self.tail = new_node
        else:
           self.tail.next = new_node
           self.tail = self.tail.next                   

   # delete from the tail
   def delete(self):

       # already empty case
       if self.head == None and self.tail == None:
           return

       # single node case (head = tail)
       if self.head == self.tail:
          self.head = None
          self.tail = None
          return

       # find next-to-last element by moving only forward
       cur = self.head
       while cur != self.tail:
           prev = cur
           cur = cur.next
       self.tail = prev
       prev.next = None


   # print full list
   def print_all (self):
       cur = self.head
       while cur != None:
          print( cur.value)
          cur = cur.next

