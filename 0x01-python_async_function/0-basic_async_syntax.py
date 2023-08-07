#!/usr/bin/env python3

"""
Basic async syntax module
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that generates a random
    delay and waits for that duration.

    Args:
        max_delay (int): The maximum delay value.
        Defaults to 10.

    Returns:
        int: The random delay value.

    """
    rng: float = random.randrange(max_delay)
    await asyncio.sleep(rng)
    return rng
