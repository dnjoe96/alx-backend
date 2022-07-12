#!/usr/bin/env python3
""" Module for BasicCache class """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class
    """
    def put(self, key, item):
        """ Method to add to cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from cache
        """
        if key:
            return self.cache_data.get(key)
