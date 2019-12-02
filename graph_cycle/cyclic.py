# cyclic()
# return true if graph has a cycle, otherise false
# note: assumes graph adjacency is defined by dictionary
#
# reference:
#    https://codereview.stackexchange.com/questions/86021/
#            check-if-a-directed-graph-contains-a-cycle
def cyclic(g):

    path = set() # path = set of nodes.vertices visited

    # DFS to detect cycles starting from node/vertex v
    def search(v):
        # if v is already in path, we've looped
        if v in path:
           return True

        path.add(v) # mark current vode.vertex as visited
        for n in g.get(v, ()): # get neighbors
            r = search(n)      # visit neightbors (recursively)
            if r == True:      # if any neighbor detects a loop...
               return r        #... then return true

        path.remove(v)         # clear path set for next search() call  
        return False           # no loops detected anywhere

    return any(search(v) for v in g) # search entire graph, starting at each node


# test on simple cyclic graph
print("Test1: cyclic ")
g = {1: (2,), 2: (3,), 3: (1,)}
r =cyclic(g)
print(r)

# test on simple acyclic graph
print("Test1: acyclic ")
g={1: (2,), 2: (3,), 3: (4,)}
r =cyclic(g)
print(r)

# test on simple cyclic graph
print("Test3: cyclic ")
g = {1: (2,), 2: (3,), 3: (4,5,), 5:(6,), 6:(1,)}
r =cyclic(g)
print(r)
