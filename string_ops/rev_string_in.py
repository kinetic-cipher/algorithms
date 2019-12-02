import math

def swap_in_place(x,y):
    x=ord(x); y = ord(y)
    x = x^y
    y = y^x
    x = x^y
    return chr(x),chr(y)

def rev_list_in_place(S):
    L = len(S)
    c = math.ceil(L/2)
    for k in range(c):
        S[k],S[L-1-k] = swap_in_place( S[k],S[L-1-k] )    

def rev_string_in_place(S):
    S_list = list(S)
    rev_list_in_place(S_list)
    S_rev = "".join(S_list)
    return(S_rev) 


S="hello"
print(S)
S_rev = rev_string_in_place(S)
print(S_rev)


