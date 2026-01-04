def merge_and_remove_duplicates(list1: list, list2: list) -> set:
    '''Merge two lists and remove duplicates.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        set: A set containing unique elements from both lists.

    Examples:
    >>> merge_and_remove_duplicates([1, 2, 2], [2, 1, 1])
    {1, 2, 1}

    >>> merge_and_remove_duplicates(["ant", "bat"], ["bat", "cat"])
    {'ant', 'bat', 'cat'}
    '''
    
    return set(list1 + list2)


# Merge and Remove Duplicates
# Given two lists list1 and list2, merge both lists and return a set with all the elements in the list1 and list2.

# Examples

# >>> merge_and_remove_duplicates([1, 2, 2], [2, 1, 1])
# {1, 2, 1}
# >>> merge_and_remove_duplicates(["ant", "bat"], ["bat", "cat"])
# {'ant', 'bat', 'cat'}
    
