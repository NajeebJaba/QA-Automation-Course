# Question 1

##################  Arrays and Strings: ##################


# q1.a:  Write a program to reverse a string in place.

# "reverse a string in place"
def reverse_string_in_place(inp_str):
    # Convert the string to a list of characters
    char_list = list(inp_str)

    # Get the length of the string
    length = len(char_list)

    # Iterate over the first half of the string
    for i in range(length // 2):
        # Swap characters from the beginning and end of the string
        char_list[i], char_list[length - 1 - i] = char_list[length - 1 - i], char_list[i]

    # Convert the list back to a string
    reverse_str = ''.join(char_list)

    return reverse_str


# Testing the function to verify if it's running well
#inp_str = "BEYOND DEV"
#result = reverse_string_in_place(inp_str)
#print(f"Original: {inp_str}")
#print(f"Reversed: {result}")


################################################################################
################################################################################

# q1.b:  Write a program to find the maximum and minimum elements in an array.
def find_max_min_elements_in_the_array(arr):
    # Check if the array is empty
    if not arr:
        return None

    # Initialize variables for minimum and maximum elements
    min_element = max_element = arr[0]

    # Iterate through the array to find minimum and maximum elements
    for element in arr:
        if element < min_element:
            min_element = element
        elif element > max_element:
            max_element = element

    return min_element, max_element


# Testing the function to verify if it's running well
#input_array = [4, 1, 33, 1, 5, 9, 2, 6, 5, 3, 5, 12, 0]
#min_value, max_value = find_max_min_elements_in_the_array(input_array)

#print(f"Input Array: {input_array}")
#print(f"Minimum Element: {min_value}")
#print(f"Maximum Element: {max_value}")


################################################################################
################################################################################

# q1.c:  Write a program to remove duplicates from a sorted array.

def remove_duplicates_from_sorted_array(sort_arr):
    # Check if the array is empty
    if not sort_arr:
        return 0

    # Initialize variables for the current and next distinct elements
    unique_index = 0

    # Iterate through the array to remove duplicates
    for i in range(1, len(sort_arr)):
        if sort_arr[i] != sort_arr[unique_index]:
            unique_index += 1
            sort_arr[unique_index] = sort_arr[i]

    # Return the new length of the array without duplicates
    return unique_index + 1


# Testing the function to verify if it's running well
#input_arr = [0, 0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 9, 9, 9, 10, 15]
#new_length = remove_duplicates_from_sorted_array(input_arr)

#print(f"Original Arr: {input_array[:new_length]}")


