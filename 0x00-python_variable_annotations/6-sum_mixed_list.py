#!/usr/bin/env python3
"""
Function: sum_list()
"""
from typing import List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function: sum_list()

    Description:
    Calculates the sum of all the elements in the input list.

    Parameters:
    - input_list (list[float]): A list of float numbers.

    Return Type:
    float: The sum of all the elements in the input list.
    """

    return sum(mxd_lst)
