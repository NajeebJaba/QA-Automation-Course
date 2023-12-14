# Question 7

##################  Recursion: ##################

# a.Write a program to calculate the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Testing the function to verify if it's running well
# num = 5
# result = factorial(num)
#
# print(f"The factorial {num} is: {result}")


##############################################################
##############################################################

# b.Write a program to generate all permutations of a string using recursion.

def generate_permutations_of_string(s):
    if len(s) <= 1:
        return [s]

    result = []
    for i in range(len(s)):
        first_char = s[i]
        remaining_chars = s[:i] + s[i + 1:]
        permutations_of_remaining = generate_permutations_of_string(remaining_chars)

        for perm in permutations_of_remaining:
            result.append(first_char + perm)

    return result


# Testing the function to verify if it's running well
# input_string = "rxy"
# result_permutations = generate_permutations_of_string(input_string)
#
# print(f"All permutations of '{input_string}': {result_permutations}")

