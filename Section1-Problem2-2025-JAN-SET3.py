def upper_nth_index_char(s: str, n: int) -> str:
    '''
    Capitalize the nth character in the given string.

    Args:
        s (str): The input string.
        n (int): The index of the character to be capitalized.

    Returns:
        str: The modified string with the nth character capitalized, or the original string if `n` is out of bounds.

    Examples:
    >>> upper_nth_index_char("hello", 1)
    'hEllo'
    >>> upper_nth_index_char("python", 3)
    'pytHon'
    >>> upper_nth_index_char("python", 9)
    'python'
    '''
    
    
    if 0 <= n < len(s): 
        return s[:n] + s[n].upper() + s[n+1:]
    return s  
    
# #Another Method
# def upper_nth_index_char(s: str, n: int) -> str:
    
#     if len(s) <= n:
#         return s 
#     else:
#         return s[0:n]+s[n].upper()+s[n+1::]
    
#    Capitalize nth Character
# You are given a string s and an integer n. Your task is to capitalize the nth character in the string s, If n is greater than the length of the string, return the string unchanged.

# Examples

# >>> upper_nth_index_char("hello", 1)
# 'hEllo'
# >>> upper_nth_index_char("python", 3)
# 'pytHon'
# >>> upper_nth_index_char("python", 9)
# 'python' 

