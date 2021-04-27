#!/usr/bin/env python3
'''
Let's execute multiple coroutines at the same time with async
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async routine called wait_n that takes in 2 int
    '''
    tasks = []
    delays = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays