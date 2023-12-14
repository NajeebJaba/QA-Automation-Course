# Question 9

##################  Bit Manipulation: ##################


#a.Write a program to check if a given number is even or odd using bit manipulation.

def is_even(number):

    return (number & 1) == 0

# Test the program
# num = 10
#
# if is_even(num):
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")

##############################################################
##############################################################


#b.Write a program to find the number of set bits in a given integer using bit manipulation.

def count_set_bits(number):

    count = 0

    while number:
        # Increment count if the least significant bit is set (1)
        count += number & 1
        # Right shift the number to check the next bit
        number >>= 1

    return count

# Test the program
# num = 40
#
# set_bits_count = count_set_bits(num)
#
# print(f"The number of set bits in {num} is: {set_bits_count}")



