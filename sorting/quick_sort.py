
import math

def partition(A, lo_idx, hi_idx):

    pivot_idx = lo_idx + math.floor( (hi_idx - lo_idx)/2 ) 
    pivot_val = A[ pivot_idx ]
 
    while True:
        # move hi and lo indexes to find a swap candidate 
        # (i.e. A[lo_idx] > pivot_val and A[hi_idx] < pivot_val
        while A[lo_idx] < pivot_val:
            lo_idx = lo_idx + 1
        while A[hi_idx] > pivot_val:
            hi_idx = hi_idx - 1
        if lo_idx >= hi_idx:
            return hi_idx

        # swap 
        tmp = A[lo_idx]
        A[lo_idx] = A[hi_idx]
        A[hi_idx] = tmp 
 
        # update hi/lo indexes
        lo_idx = lo_idx + 1
        hi_idx = hi_idx - 1
        

def quick_sort( A, lo_idx, hi_idx):
    if lo_idx < hi_idx:
        pivot_idx = partition(A, lo_idx, hi_idx)
        quick_sort(A, lo_idx, pivot_idx)
        quick_sort(A, pivot_idx+1, hi_idx)



# test
my_list = [5,9,11,2,23,0,4,17,7,3]
print(my_list)
quick_sort(my_list,0,len(my_list)-1)
print(my_list)



