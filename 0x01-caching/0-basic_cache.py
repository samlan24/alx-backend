#!/usr/bin/python3
"""class that inherits BaseCaching"""
from base_caching import BaseCaching


class BasicCache (BaseCaching):
    """this is a basic cache class"""
    def __init__(self):
        """using super to call the parent class"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
