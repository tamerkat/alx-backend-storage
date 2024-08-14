#!/usr/bin/env python3
"""main file"""


import redis
from uuid import uuid4
from typing import Union


class Cache:
    """cache"""
    def __init__(self):
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        """store"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key
