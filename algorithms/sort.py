# Repeatedly selects the smallest or largest element from
# the unsorted position of the list and moving it to the
# sorted position of the list. It is simple and easy to
# understand and works well with small databases, but it
# is not stable and has a worst-case O(n^2) time
def selection_sort(arr):

    for i in range(len(arr) - 1):

        min_idx = i
        
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Repeatedly swaps adjacent elements if they are in the
# wrong order. It is easy to understand and implement,
# does not require any additional memory space, and is
# stable. However, it has a time complexity of O(n^2)
# and is a comparison-based algorithm which can limit
# its efficiency in certain cases
def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(o, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if (swapped == False):
            break

# O(n^2)
def rec_bubble_sort(arr):

    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    rec_bubble_sort(arr)

# Works by building a sorted array one element at a
# time. Does not require any additional memory space.
# It is simple, stable, efficient for small lists, and
# adoptive. However, it is inefficient for large lists.
# O(n^2) time complexity
def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]

        arr[j + 1] = key

# Merges two subarrays of array[]
def merge(arr, left, mid, right):

    sub_array_one = mid - left + 1
    sub_array_two = right - mid
    left_array = [0] * sub_array_one
    right_array = [0] * sub_array_two

    for i in range(sub_array_one):
        left_array[i] = arr[left + i]
    for j in range(sub_array_two):
        right_array[j] = arr[mid + 1 + j]

    index_sub_array_one = 0
    index_sub_array_two = 0
    index_merged_array = left

    while index_sub_array_one < sub_array_one and index_sub_array_two < sub_array_two:
        
        if left_array[index_sub_array_one] <= right_array[index_sub_array_two]:
            arr[index_merged_array] = left_array[index_sub_array_one]
            index_sub_array_one += 1
        else:
            arr[index_merged_array] = right_array[index_sub_array_two]
            index_sub_array_two += 1
        
        index_merged_array += 1

    while index_sub_array_one < sub_array_one:

        arr[index_merged_array] = left_array[index_sub_array_one]
        index_sub_array_one += 1
        index_merged_array += 1

    while index_sub_array_two < sub_array_two:

        arr[index_merged_array] = right_array[index_sub_array_two]
        index_sub_array_two += 1
        index_merged_array += 1

# Follows the divide-and-conquer approach by recursively
# dividing the input array into smaller subarrays and
# sorting the subarrays before merging them back together.
# Begin for left index and end for right index
def merge_sort(arr, begin, end):

    if begin >= end:
        return
    
    mid = begin + (end - begin) // 2
    merge_sort(arr, begin, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, begin, mid, end)

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j, arr[i]])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1

# Picks an element as a pivot and partitions the given
# array around the pivot by placing it in its correct
# position in the sorted array
def quick_sort(arr, low, high):

    if low < high:

        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def heapify(arr, N, i):

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)

# Comparison-based sorting technique based on binary heap
# data structure. It is similar to the selection sort. It
# is costly, unstable, and inefficient for large amounts of
# data, but simple and uses minimal memory with an efficient
# time complexity.
def heap_sort(arr):

    N = len(arr)

    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Counting sort is a non-comparison-based sorting algorithm.
# It is efficient when the range of input values is small
# compared to the number of elements to be sorted. The idea
# is to count the frequency of each distinct element in the
# input array and use the information to place the elements
# in their correct positions. Counting sort is generally faster
# than all comparison-based algorithms if the range of input
# is of the order of the number of input, and it is stable.
# It does not work on decimal values, is inefficient if the
# range of values is very large, and uses extra space for
# sorting the array elements.
def counting_sort(arr):

    max = max(arr)

    count_array = [0] * (max + 1)

    for num in arr:
        count_array[num] += 1

    for i in range(1, max + 1):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        output_array[count_array[arr[i]] - 1] = arr[i]
        count_array[arr[i]] -= 1
    
    return output_array

# Radix sort is a linear sorting algorithm that sorts elements
# by processing them digit by digit. It is an efficient sorting
# algorithm for integers or strings with fixed-size keys.
def radix_count(arr, exp1):

    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):

    max1 = max(arr)
    exp = 1

    while max1 / exp >= 1:
        radix_count(arr, exp)
        exp *= 10

# Involves dividing elements into various buckets formed
# by uniformly distributing the elements. Once the elements
# are divided, they can be sorted using any other sorting
# algorithm
def bucket_sort(arr):

    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0

    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1