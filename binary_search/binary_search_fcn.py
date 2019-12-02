import math

def f(x):
   return 1+x**2 # monotonic function = "sorted array"

def find_idx(y_target,f):
    n1 = 0
    n2 = 100
   
    while True:
       m = math.floor((n1+n2)/2) # new test point
       #print(m)

       if f(m) < y_target:
          n1 = m + 1   # too low, bring lower bound up
       elif f(m) > y_target:
          n2 = m - 1   # too high, bring upper bound down
       else:
          return m          

n_target = find_idx(5,f)
print(n_target)

 
        




