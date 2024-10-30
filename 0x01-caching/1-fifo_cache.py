#!/usr/bin/env python3
"""fifo caching module"""
from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """FIFOCache class definition"""
    def __init__(self):
        """inherits from parent class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put method"""
        if key and item:

            if key not in self.cache_data:
                self.order.append(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """get method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
