
# returns True if strings are anagrams or each other
def anagram_compare(my_string1, my_string2):
    my_list1 = list(my_string1)
    my_list2 = list(my_string2)
    L1 = len(my_list1)
    L2 = len(my_list2)
    mask = [0]*L1  
 
    if len(my_list1) != len(my_list2):
       return False
    else:
       L = len(my_list1)                                                                                                                                                                                                                                                 
    for k in range(L):
       for n in range(L):
          if mask[n] != 0:
              continue
          if my_list1[k] == my_list2[n]:
             mask[n] = 1  # match! exclude next time    

    if sum(mask) == L1:
       return True
    else:
       return False 


# test

my_string1 = "hello"
my_string2 = "elolh"
is_ana = anagram_compare(my_string1, my_string2)
print(is_ana)


