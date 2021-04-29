#!/usr/bin/env python3
'''
1. Async Comprehensions
'''

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Coroutine will collect 10 random numbers
    '''

    return [number async for number in async_generator()]
