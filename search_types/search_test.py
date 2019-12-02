import node as n
import bfs_search as bfs
import dfs_search as dfs

# create a binary tree
r = n.Node(1)
r.left = n.Node(2)
r.right = n.Node(3)
r.left.left = n.Node(4)
r.left.right = n.Node(5)
r.right.left = n.Node(6)
r.right.right = n.Node(7)

# print tree using depth-frst search
print("depth-first traversal")
dfs = dfs.DfsSearch()
dfs.search(r)

print("-----")

# print teree using depth-first search
print("breadth-first traversal")
bfs = bfs.BfsSearch()
bfs.search(r)


