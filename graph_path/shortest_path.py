# shortest_path:
#
# example variant of Djikstra's algorihtm
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 
#

# minimum distance node in Q
def min_dist_node(S,D):
      u = None
      d_min = min( [D[v] for v in S] )
      for v in S:
        if D[v] == d_min:
           u = v
           break
      return u

# initalize all distances (to source)
def init(g,s,D,S):
  # assign distances to all nodes...
  # ...and place in not-visited queue  
  for v in g:
     S.add(v)
     if v == s:
        D[v] = 0
     else:
        D[v] = float("Inf")


# Find shortest path in graph g from sourcenode s
def shortest_path(g,s):
  # init 
  P = {}          # previous node sequence
  S = set()       # set of all unvisited nodes
  D = {}          # distanves
  init(g,s,D,S)   # initialize distances 

  # process all nodes/vertices in the unvisited set 
  while len(S) > 0: 
      u = min_dist_node(S,D)

      for v in g.get(u,()):
         D_test = D[u] + g[u][v]
         if D_test < D[v]:
             D[v] = D_test 
             P[v] = u

      S.remove(u) # consume element

  # return sequence of nodes (a min path)
  return D,P


# test--get distances to all nodes and previous nodes
g = { '1':{'2':3, '3':1}, '2':{'4':5,'5':2}, '3':{'5':3}, '4':{}, '5':{} }
D,P = shortest_path(g,'1')
print("D: (distances) ",D)
print("P: (previous nodes)",P)


# print a shortest path, t = target (end) node...
# P = prev list returned from shortest path
def get_shortest_path(t,P):
    node_seq = list()
    node_seq.append(t)
    while t != None and t in P:
       t = P[t]
       node_seq.append(t)

    node_seq.reverse()
    return node_seq


# return a best/shortest path termination at target node t
print("shortest path: ")
t = '5'
seq = get_shortest_path(t,P)
print(seq)



