def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
        
    return -1

# Divide the search space into two halves by finding
# the middle index
def binary_search(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Recursive binary search
def rec_binary_search(arr, low, high, x):

    if high >= low:

        mid = low + (high - low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return rec_binary_search(arr, low, mid - 1, x)
        else:
            return rec_binary_search(arr, mid + 1, high, x)
    
    else:
        return -1
    