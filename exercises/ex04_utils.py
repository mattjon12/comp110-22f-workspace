"""List utility functions exercise"""

__author__ = "730382085"

def all(list_of_integers: list[int], one_integer: int) -> bool:
    """This function checks the whether the length of list is TRUE or FALSE."""
    list_length: int = len(list_of_integers)
    index_parser: int = 0
    result: bool = True
    while index_parser != list_length:
        if list_of_integers[index_parser] != one_integer:
            result = False
        index_parser = index_parser + 1
    if  list_length <= 0:
        result = False
    if result == False:
        return False
    if result == True:
        return True

def max(input: list[int]) -> int: 
    """This function returns the largest integer in the list."""
    max_index_parser: int = 0
    integer: int = input[max_index_parser]
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    while max_index_parser != len(input):
        if integer < input[max_index_parser]:
            integer = input[max_index_parser]
        max_index_parser = max_index_parser + 1 
    return integer

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """This function will determine whether the two lists are equal to one another or not."""
    if len(list_one) != len(list_two):
        return False 
    is_equal_bool: bool = True
    is_equal_index_parser: int = 0

    while is_equal_index_parser != len(list_one):
        if list_one[is_equal_index_parser] != list_two[is_equal_index_parser]:
            is_equal_bool = False
        is_equal_index_parser = is_equal_index_parser + 1

    if is_equal_bool == True:
        return True
    if is_equal_bool == False:
        return False
  