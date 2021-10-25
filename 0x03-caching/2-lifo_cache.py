#!/usr/bin/env python3
"""class FIFOCache inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """first in first out caching"""

    def __init__(self):
        """what is overloading?"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """track order added w/ self.order"""
        if (key is not None and item is not None):
            if (key in self.cache_data):
                self.cache_data[key] = item
            else:
                if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                    yeet = self.order.pop()
                    self.cache_data.pop(yeet)
                    print("DISCARD: " + yeet)
                self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """rtn item by key"""
        if (key is not None and key in self.cache_data):
            return self.cache_data[key]
        return None
