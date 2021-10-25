#!/usr/bin/env python3
"""class FIFOCache inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching



class FIFOCache(BaseCaching):
    """first in first out caching"""
    def __init__(self):
        """what is overloading?"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """track order added w/ self.order"""
        if (key is not None and item is not None):
            if (len(self.order) < BaseCaching.MAX_ITEMS):
                self.order.append(key)
                self.cache_data[key] = item
            else:
                if(key not in self.cache_data):
                    yeet = self.order.pop(0)
                    self.order.append(key)
                    self.cache_data.pop(yeet)
                    self.cache_data[key] = item
                    print("DISCARD: " + yeet)

    def get(self, key):
        """rtn item by key"""
        if (key is not None and key in self.cache_data):
            return self.cache_data[key]
        return None
