#!/usr/bin/env python3
"""Writing str to redis"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """counts calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """call hist"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush("{}:inputs".format(key), str(args))
        value = method(self, *args)
        self._redis.rpush("{}:outputs".format(key), value)
        return value
    return wrapper


def replay(method: Callable) -> Callable:
    """
    Function decorator for Cache class
    """
    redis = method.__self__._redis
    name = method.__qualname__
    print("{} was called {} times:".format(name,
                                           redis.get(name).decode('utf-8')))
    inputs = redis.lrange("{}:inputs".format(name), 0, -1)
    outputs = redis.lrange("{}:outputs".format(name), 0, -1)
    full = list(zip(inputs, outputs))
    for inp, output in full:
        print("{}(*{}) -> {}".format(name, inp.decode('utf-8'),
                                     output.decode('utf-8')))


class Cache():
    """cashe class"""
    def __init__(self):
        """init class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """take data and rtn str"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[callable] = None) -> str:
        """https://docs.python.org/3/library/typing.html"""
        req = self._redis.get(key)
        if fn:
            return fn(req)
        return(req)

    def get_str(self, key) -> str:
        """get str"""
        req = self._redis.get(key)
        return req.decode('utf-8')

    def get_int(self, key) -> int:
        """get int"""
        req = self._redis.get(key)
        return int.from_bytes(req, sysbyteorder)
