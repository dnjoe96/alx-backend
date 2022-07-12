#!/usr/bin/env python3
""" LIFOCache Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Class Implementing FIFO"""
    def __int__(self):
        """ class constructor"""
        super().__init__()

    def put(self, key, item):
        """ Method to add to cache
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lastItemKey = list(self.cache_data.keys())[-1]
                self.cache_data.pop(lastItemKey)
                print('DISCARD: {}'.format(lastItemKey))
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from cache
        """
        if key:
            return self.cache_data.get(key)
