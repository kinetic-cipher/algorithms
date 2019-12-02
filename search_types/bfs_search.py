import node as nd

# breadth-first search
class BfsSearch:

    # init--set up a queue
    def __init__(self):
       self.Q = list()

    # process a node (print)
    def process(self, node):
       if node != None:
           print(node.val)
   
    # perform iterative search
    def search(self, node):
        Q = self.Q         # local alias
        self.process(node) # process the root node
        Q.append(node)     # add root node to END (newest datai)--to process children       
  
        while( len(Q) > 0):
           n = Q[0]; Q = Q[1:len(Q)]      # consume from FRONT (oldest data)
           self.process(n.left)           # process child
           self.process(n.right)          # process child
           if n.left != None:             # validate
               Q.append(n.left)           # queue child to process grand-children next loop
           if n.right != None:            # validate
               Q.append(n.right)          # queue child to process grand-children next loop

