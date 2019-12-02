
import binary_tree as bt
import binary_node as bn

T = bt.BinaryTree(1)
T.add_node(2, T.root, 0)       # create T.toot.left
T.add_node(3,T.root, 1)        # create T.root.right
T.add_node(4, T.root.left, 0)  # create T.root.left.left
T.print_all(T.root)



