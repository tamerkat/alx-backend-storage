#!/usr/bin/env python3
"""main file"""


import redis
from uuid import uuid4
from typing import Union, Optional


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

    def get(self, key: str, fn: Optional[callable[[bytes], Union[str, float, bytes, int]]] = None) -> Union[int, float, bytes, None, str]:
        data = self.get(key)

        if data is None:
            return None
        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: int) -> Optional[int]:
        return self.get(key, lambda data: int(data))
