#!/usr/bin/env python3

"""
Module: add

"""


def add(a: float, b: float) -> float:
    """
    Function: add()

    Description:
    Returns the sum of two floating-point numbers, 'a' and 'b'.

    Parameters:
    - a (float): The first floating-point number to be added.
    - b (float): The second floating-point number to be added.

    Return Type:
    float: The sum of 'a' and 'b' as a floating-point number.

    The add() function is specifically designed to work with
    floating-point arguments and returns the sum as a float
    to accommodate cases where the sum may result in a non-integer value.
    """
    return a + b
