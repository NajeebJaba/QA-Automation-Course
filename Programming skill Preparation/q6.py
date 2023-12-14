# Question 6

##################  Searching Algorithms: ##################

# a.Implement the linear search algorithm.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Testing the function to verify if it's running well
# arr = [68, 34, 25, 13, 22, 12, 80]
# target_element = 22
#
# result = linear_search(arr, target_element)
#
# if result != -1:
#     print(f"Element {target_element} found at index {result}.")
# else:
#     print(f"Element {target_element} not found.")


##############################################################
##############################################################

# b.Implement the binary search algorithm

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Target element found
        elif mid_element < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target element not found


# Testing the function to verify if it's running well
# sorted_array = [68, 34, 25, 13, 22, 12, 80]
# target_element = 22
#
# result = binary_search(sorted_array, target_element)
#
# if result != -1:
#     print(f"Element {target_element} found at index {result}.")
# else:
#     print(f"Element {target_element} not found.")

