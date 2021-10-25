#!/usr/bin/env python3
"""class BasicCache inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a caching system"""
    def put(self, key, item):
        """add item to cach with key as value"""
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """rtn item by key"""
        if (key is not None and key in self.cache_data):
            return self.cache_data[key]
        return None
