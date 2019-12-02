import math

# reverse using inex swapping
def rev_list(input_list):
    L = len(input_list)
    c = math.ceil(L/2)

    # swap
    for k in range(c):
       tmp = input_list[k]
       input_list[k] = input_list[L-1-k]
       input_list[L-1-k] = tmp


# original list  
my_list = [1,2,3,4,5]
print(my_list)

# reverse using index swapping
rev_list(my_list)
print(my_list)

# reverse using list comprehension
my_list = [1,2,3,4,5]  # start again (since we already reversed it)
L = len(my_list)
my_rev_list = [ my_list[ L-1-k ] for k in range(L)  ]
print(my_rev_list)


