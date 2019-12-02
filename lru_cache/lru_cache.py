import node as n

# Laest-Recently Used Cache
class LRUCache:

   # constructor 
    def __init__(self,max_items):
        self.hash_map = dict() 
        self.num_items = 0  
        self.max_items = max_items 
        self.front = None # most used
        self.back = None   # least used

    # add node to front (make it most recently used)
    def _add_node_to_front(self,new_node):
        if self.front == None:
           self.front = new_node
           self.back = new_node
        else:
           self.front.prev = new_node
           new_node.next = self.front
           self.front = new_node    
           self.front.prev = None

        self.num_items = self.num_items + 1 
 
    # remove node from linked list
    def _remove_node(self,node):
       if node == self.front:  # shouldn't happen
          self.front = node
          node.prev = None
       elif node == self.back:  # evicting least-recently used node
           self.back = self.back.prev
           self.back.next = None
       else:  # middle--happens when moving a node to front
          node.prev.next = node.next 
          node.next.prev = node.prev

       self.num_items = self.num_items - 1 
 
    # process the given input item/value
    def process_item( self, x):
       # case 1: in cache--find node via hashmap and move to front 
       h = hash(x)  # not necessary if x is integer
       if h in self.hash_map:
          node = self.hash_map[h]
          if node != self.front: 
              self._remove_node(node)         # (move node to front)
              self._add_node_to_front(node)   # (move node to front)
              # self.hashmap[h] = node   # no need to update hash_map on move

       # case 2: not in cache, cache full-- remove end node, add new node to front, update hashmap
       # case 3: not in cache, cache not full--add node to front & update hashmap
       else:
           new_node = n.Node(x)
           if self.num_items >= self.max_items:  # cache is full, evict
               self._remove_node(self.back)   
               del self.hash_map[hash(self.back.val)] 

           # most recently used node
           self._add_node_to_front(new_node)
           self.hash_map[ hash(x) ] = new_node                  


    # print out the cache contents 
    def print_all(self):
        cur = self.front
        while cur != None:
           print( cur.val )
           cur = cur.next
            
    
