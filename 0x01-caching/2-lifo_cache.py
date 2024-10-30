#!/usr/bin/env python3
"""lifo cache module"""
from base_caching import BaseCaching


class LIFOCache (BaseCaching):
    """initializing LIFOCache class"""
    def __init__(self):
        """inheritance from parent class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put method"""
        if key and item:

            if key not in self.cache_data:
                self.order.append(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                latest_item = self.order.pop()
                del self.cache_data[latest_item]
                print(f"DISCARD: {latest_item}")

    def get(self, key):
        """get method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
