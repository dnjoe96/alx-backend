#!/usr/bin/env python3
""" FIFOCache Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Class Implementing FIFO"""
    def __int__(self):
        """ class constructor"""
        super().__init__()

    def put(self, key, item):
        """ Method to add to cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                firstItemKey = list(self.cache_data.keys())[0]
                self.cache_data.pop(firstItemKey)
                print('DISCARD: {}'.format(firstItemKey))

    def get(self, key):
        """ Retrieve an item from cache
        """
        if key:
            return self.cache_data.get(key)
