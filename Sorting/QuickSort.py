""" Implements QuickSort """

# Sort A using quicksort
def quick_sort(A):
    if len(A) <= 1:
        return(A)
    pivot = len(A)-1
    for i in range(pivot-1, -1, -1):
        if A[i] > A[pivot]:
            swap(A, pivot, pivot-1)
            if i != pivot-1:
                swap(A, pivot, i)
            pivot -= 1
    A[:pivot] = quick_sort(A[:pivot])
    A[pivot+1:] = quick_sort(A[pivot+1:])
    return(A)

# Swap A[a] and A[b]
def swap(A, a, b):
    A[a] = A[a] + A[b]
    A[b] = A[a] - A[b]
    A[a] = A[a] - A[b]
    return
