def is_even_and_second_last_digit_is_two(num: int) -> bool:
    '''
    Check if a number is even and if the second last digit is two.

    Args:
        num (int): The integer to check.

    Returns:
        bool: Returns True if the number is even and the second last digit is 2, False otherwise.
    '''
    
    return num % 2 == 0 and abs(num) // 10 % 10 == 2
# #Another Method:

# def is_even_and_second_last_digit_is_two(num: int) -> bool:
#     if num%2==0 and str(num)[-2]=='2':
#         return True
#     else:
#         return False
    
# Check Even Number and Second Last Digit is Two
# Write a function is_even_and_second_last_digit_is_two that takes an integer input num and returns a boolean value. The function should check if the number is even and if the second last digit is two. If both conditions are satisfied, return True; otherwise, return False.

# Examples

# >>> is_even_and_second_last_digit_is_two(232)
# False
# >>> is_even_and_second_last_digit_is_two(120)
# True
# >>> is_even_and_second_last_digit_is_two(25)
# False
# >>> is_even_and_second_last_digit_is_two(13)
# False
