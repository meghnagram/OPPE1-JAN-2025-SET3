def replace_vowels_with_next_alphabet(s: str) -> str:
    """
    Replaces all vowels in the input string with the next character in the alphabet.

    Args:
        s (str): The input string to process.

    Returns:
        str: A string with all vowels replaced by their next alphabetical character.
    
    Note:
        This function is case-sensitive.
    
    Examples:
        >>> replace_vowels_with_next_alphabet("hello")
        'hflmp'
        >>> replace_vowels_with_next_alphabet("HELLO")
        'HFLMP'
    """
    
     
    vowels = "aeiouAEIOU"
    result = []
    for char in s:
        if char in vowels:
            result.append(chr(ord(char) + 1))
        else:
            result.append(char)
    return ''.join(result)

# #Another method:
# def replace_vowels_with_next_alphabet(s: str) -> str:
#     a=''
#     for i in s:
#         if i.lower() in ('a','e','i','o','u'):
#             a=a+chr(ord(i)+1)
#         else:
#             a=a+i
            
#     return a

# Replace Vowels with Next Alphabet
# You are given a string s. Your task is to replace each vowel in the string with the next letter in the alphabet while keeping the rest of the characters unchanged.

# Note: The function is case-sensitive. For example, a is replaced with b, and A is replaced with B.
    


    
