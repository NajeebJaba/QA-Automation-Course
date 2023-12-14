# Question 5

##################  Sorting Algorithms: ##################

# a.Implement the bubble sort algorithm.
def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Testing the function to verify if it's running well
# unsorted_array = [68, 34, 25, 13, 22, 12, 80]
# sorted_array = bubble_sort(unsorted_array)
#
# print("Unsorted Array:", unsorted_array)
# print("Sorted Array:", sorted_array)


##############################################################
##############################################################

# b. Implement the merge sort algorithm.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append the remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Testing the function to verify if it's running well
# unsorted_array = [68, 34, 25, 13, 22, 12, 80]
# sorted_array = merge_sort(unsorted_array)
#
# print("Unsorted Array:", unsorted_array)
# print("Sorted Array:", sorted_array)


##############################################################
##############################################################

# c.Implement the quicksort algorithm.
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Testing the function to verify if it's running well
# unsorted_array = [68, 34, 25, 13, 22, 12, 80]
# sorted_array = quicksort(unsorted_array)
#
# print("Unsorted Array:", unsorted_array)
# print("Sorted Array:", sorted_array)
