""" Implementation of bubble sort """

def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            #print("for i = {}, j = {}".format(i, j))
            #print(A)
            if A[j] > A[j+1]:
                swap(A, j, j+1)
            #print(A)
            #print()
    return(A)

# Swap A[a] & A[b] in list A
def swap(A, a, b):
    #print("swapping A[{}] and A[{}]".format(a, b))
    A[a] = A[a] + A[b]
    A[b] = A[a] - A[b]
    A[a] = A[a] - A[b]
    return(A)
