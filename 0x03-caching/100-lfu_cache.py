#!/usr/bin/env python3
"""class FIFOCache inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """first in first out caching"""

    def __init__(self):
        """what is overloading?"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """track order added w/ self.order"""
        if (key is not None and item is not None):
            self.cache_data[key] = item
            if (key in self.order):
                self.order.remove(key)
                self.order.append(key)
            else:
                self.order.append(key)
            if (len(self.order) > BaseCaching.MAX_ITEMS):
                i = BaseCaching.MAX_ITEMS - 1
                yeet = self.order.pop(i)
                del self.cache_data[yeet]
                print("DISCARD: " + yeet)

    def get(self, key):
        """rtn item by key"""
        if (key is not None and key in self.order):
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
