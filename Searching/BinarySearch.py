# Search for value in input_array
def binary_search(input_array, value):
    left = 0
    right = len(input_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if input_array[mid] == value:
            return(mid)
        elif input_array[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return(-1)
