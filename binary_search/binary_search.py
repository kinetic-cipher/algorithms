import math

def binary_search( my_list, target_val):

   n1 = 0
   n2 = len(my_list) - 1

   while n1 <= n2:    
      m = math.floor( (n1+n2)/2 ) # test point
      if my_list[m] < target_val:
          n1 = m + 1  # too low, move lower bound up
      elif my_list[m] > target_val:
          n2 = m - 1  # too high, bring upper bound down
      else:
         return m

   return -1


# test binary search function
my_list = [1,2,3,5,7,10,11,13,15,18,20]
idx = binary_search( my_list, 13)
print(idx)

