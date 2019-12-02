import node as nd

# depth-first search
class DfsSearch:

    # inite
    def __init__(self):
        self = self

    # process a node (print)
    def process(self, node):
        if node != None:
            print(node.val)
   
    # perform iterative search
    def search(self, node):
        if node != None:
            self.process(node)
        if node.left != None:
           self.search(node.left)
        if node.right != None:
           self.search(node.right)


