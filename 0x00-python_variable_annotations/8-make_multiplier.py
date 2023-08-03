#!/usr/bin/env python3
""" Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function: make_multiplier()

    Description:
    Returns a function that multiplies a given float number by a specified multiplier.

    Parameters:
    - multiplier (float): The multiplier to be used for the multiplication.

    Return Type:
    Callable[[float], float]: A function that accepts a float number and returns the result of multiplying it by the multiplier.

    """

    def fn(n: float) -> float:
        """
        Inner function: fn()

        Description:
        Multiplies the input float number by the multiplier.

        Parameters:
        - n (float): The float number to be multiplied.

        Return Type:
        float: The result of multiplying the input number by the multiplier.
        """
        return n * multiplier

    return fn
