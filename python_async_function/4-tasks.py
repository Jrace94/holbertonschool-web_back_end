#!/usr/bin/env python3
"""Async and await syntax"""
import asyncio
from typing import List

get = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that returns a list"""
    l_async = [get(max_delay) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(l_async)]
    return finish
