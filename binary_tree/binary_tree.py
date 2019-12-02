import binary_node as bn

class BinaryTree:

    # initialize tree with root node set to specified value
    def __init__(self, value):
        self.root = bn.BinaryNode(value)
        self.root.left =  None
        self.root.right = None

    # add a child node at the given parent node
    def add_node(self, value, node, child): 
        try:
           if child == 0:
               node.left = bn.BinaryNode(value)
           elif child == 1:
               node.right = bn.BinaryNode(value)
        except:
            print("WARNING: attempted to add child to non-existent node")

    # print the tree recursively 
    def print_all(self,node):
        print (node.value)
        if node.left != None:
            self.print_all( node.left)
        if node.right != None:
            self.print_all( node.right)

