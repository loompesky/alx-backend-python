#!/usr/bin/env python3
"""
Function: sum_list()
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function: sum_list()

    Description:
    Calculates the sum of all the elements in the input list.

    Parameters:
    - input_list (list[float]): A list of float numbers.

    Return Type:
    float: The sum of all the elements in the input list.
    """

    return sum(input_list)
