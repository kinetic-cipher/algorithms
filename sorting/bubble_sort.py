
def bubble_sort(my_list):
    L = len(my_list)
    Finished = False

    while not Finished:
       # this pass
       num_swaps = 0
       for k in range(1,L):
          if my_list[k] < my_list[k-1]:
              # swap 
              tmp = my_list[k]
              my_list[k] = my_list[k-1]
              my_list[k-1]= tmp
              num_swaps = num_swaps+1

       if num_swaps == 0:
          Finished = True


my_list = [9,3,1,23,17,77,0]
print(my_list)
bubble_sort(my_list)
print(my_list)


  
