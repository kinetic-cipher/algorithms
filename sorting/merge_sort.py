# MergeSort
#
# Recursively splits into (left, right) sublists (down to length 1) and then
# recursively merges back up to a single list, with the sorting occurring
# during the merge. 
#
import math

# merge two sublists
def merge(left_list, right_list):
    result = list()

    # merge sublists 
    # left and righr sub-lists are potential sources, 'result' is the 
    #   destination list
    while( len(left_list) > 0 and len(right_list) > 0 ):

       len_left = len(left_list)
       len_right = len(right_list)

       if left_list[0] < right_list[0]:
          result.append( left_list[0] )

          # consume element, now left_list = remainder of list
          if len(left_list) > 1:
             left_list = left_list[1:len_left] # consume element just placed in result
          else:
             left_list = []
       else:
          result.append( right_list[0] )

          # consume element, now right list = remainder of list
          if len(right_list ) > 1:
             right_list = right_list[1:len_right] # consume element just placed in result
          else:
             right_list = []

    # one of the sub-lists has been consumed, now we mnust
    # finished comsuming the other (only one of the for-loops will be active)
    for k in range( len(left_list) ):
       result.append( left_list[k] )
    for k in range( len(right_list) ):
       result.append( right_list[k] )
 
    return result


# recursive mergesort function 
def merge_sort( my_list ):
   # length-1 lists are sorted  
    L = len(my_list)
    if L <= 1:
        return my_list

    # create lieft and right sub-lists
    m = math.floor(L/2)
    left_list = my_list[0:m]   # left sub-list (note: m is not included in interval)
    right_list = my_list[m:L]  # right sub-list (note: m is included in interval)

    # sorr the sub-lists
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
 
    # merge then
    return merge(left_list, right_list)


# test
my_list = [11,2,9,13,100,33,17,45,64,77]
print(my_list)
my_sorted_list = merge_sort(my_list)
print(my_sorted_list)



