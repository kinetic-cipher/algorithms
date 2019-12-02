import node as nd


# create a tree and print it out
t = nd.Node(1)
t.left = nd.Node(2)
t.right = nd.Node(3)
t.left.left = nd.Node(4)
t.left.right = nd.Node(5)
t.right.left = nd.Node(6)
t.right.right = nd.Node(7)
t.print_all()
print("-----")


# invert tree() = reflect recursively
def invert_tree(t):

   # swap child sub-trees 
    tmp = t.left
    t.left = t.right
    t.right = tmp

    # invert child subtrees recursively
    if t.left != None:
      t.left = invert_tree(t.left)
    if t.right != None:
      t.right = invert_tree(t.right)
      
    return t

# print inverted tree
t_inv = invert_tree(t)
t_inv.print_all()


