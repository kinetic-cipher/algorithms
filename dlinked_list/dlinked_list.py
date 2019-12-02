
import node as nd


class DLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # insert(): insert at tail
    def insert(self,value):

       # create new (isolated) node
       new_node = nd.Node(value)
       new_node.next = None  
       new_node.prev = None

       # empty list case
       if self.head == None and self.tail == None:
          self.head = new_node
          self.tail = new_node 
          return

       # connect new node to the tail 
       new_node.prev = self.tail
       self.tail.next = new_node
       self.tail = new_node       


    # delete(): delete from tail
    def delete(self):
       # single element case
       if self.head == self.tail:
           self.head = None
           self.tail = None
       else:    # more than one element  
          self.tail = self.tail.prev
          self.tail.next = None

    # print_all()
    def print_all(self):
        cur = self.head
        while cur != None:
           print(cur.value)
           cur = cur.next


        
  
