""" Recursive implementation of merge sort """

# Recursively divide the list in two halves and then merge both the halves
def merge_sort(A):
    if len(A) == 1:
        return(A)
    mid = len(A) // 2
    leftA = merge_sort(A[ : mid])
    rightA = merge_sort(A[mid : ])
    mergedA = merge(leftA, rightA)
    return(mergedA)

# Merge two sorted subarrays into one sorted array
def merge(leftA, rightA):
    l_head = r_head = 0
    mergedA = []
    while l_head < len(leftA) and r_head < len(rightA):
        if leftA[l_head] < rightA[r_head]:
            mergedA = mergedA + [leftA[l_head]]
            l_head += 1
        else:
            mergedA = mergedA + [rightA[r_head]]
            r_head += 1
        if l_head == len(leftA):
            mergedA = mergedA + rightA[r_head : ]
            break
        elif r_head == len(rightA):
            mergedA = mergedA + leftA[l_head : ]
            break
    return(mergedA)

# Temporary test code
import random
A = random.sample(range(101), 11) * 2
print(merge_sort(A))