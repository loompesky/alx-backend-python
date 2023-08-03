#!/usr/bin/env python3
"""
    Function: to_kv()

"""
from typing import Union, Tuple



def to_kv(k: str, v: union[int, float]) -> Tuple[str, float]:
    """
    Function: to_kv()

    Description:
    Converts a key-value pair into a tuple.

    Parameters:
    - k (str): The key.
    - v (int or float): The value, which can be either an integer or a float.

    Return Type:
    tuple: A tuple containing the key-value pair.
    """

    return (k, v * v)
