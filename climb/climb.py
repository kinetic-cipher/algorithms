import math
import time

# compute the number of possible paths for
# n steps taking 1 or 2 at a time.
def climb(n,p):
    #print(n,p)
    if n == 0:   # no more steps = leaf = end of a path
       p = p+1   # increment the number of paths
       return p
    if n == 1:   # if there's just 1 step left we must take it
       p = climb(n-1,p)
    else:
       p1 = climb(n-1,p) # can take 1 step...
       p2 = climb(n-2,p) # ... or 2 steps
       p = p1+p2
    return p 


# compute the number of possible paths for
# n steps taking 1 or 2 at a time.
# --dynamic programming (DP) version
def climb_dp(n,p,t):
    #print(n,p)
    if n == 0:
       p = p+1
       return p
    if n == 1:
       p = climb_dp(n-1,p,t)
    else:
       if t[n-1] > 0: # already in cache
          p1 = t[n-1]
       else:
          p1 = climb_dp(n-1,p,t)
          t[n-1] = p1 # put in cache for later
       
       if t[n-2] > 0: # already in cache
          p2 = t[n-2]
       else:
          p2 = climb_dp(n-2,p,t)
          t[n-2] = p2 # put in cache for later

       p = p1+p2
    return p 


# test #1
p = 0; n = 30
start_time  = time.time()
p = climb(n,p)
run_time = time.time() - start_time
print("test 1")
print(p)
print( '%.6f sec' %(run_time))
run_time1 = run_time

# test #2
p = 0; n = 30; t = [-1]*100
start_time  = time.time()
p = climb_dp(n,p,t)
run_time = time.time() - start_time
print("test 2")
print(p)
print( '%.6f sec' %(run_time))
run_time2 = run_time


# speed up
print("DP version is %.2f times faster" %( run_time1/run_time2) )
