#!/usr/bin/env python3
""" LFUCache Module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Class Implementing LFU"""
    used = {}

    def __int__(self):
        """ class constructor"""
        super().__init__()

    def put(self, key, item):
        """ Method to add to cache
        """
        if key and item:
            # print('PUT ITEM {} >>>'.format(key))

            if len(self.cache_data) >= self.MAX_ITEMS:
                itemKeyToDiscard = \
                    sorted(self.used.items(), key=lambda x: x[1])[0][0]

                self.cache_data.pop(itemKeyToDiscard)
                self.used.pop(itemKeyToDiscard)
                print('DISCARD: {}'.format(itemKeyToDiscard))
                # print('>>>>>>>>>>>>>>>', itemKeyToDiscard)
            if not self.used.get(key):
                self.used[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from cache
        """
        if key:
            # print('GET ITEM {} >>>'.format(key))
            # print(self.used)
            if self.used.get(key) is not None:
                self.used[key] += 1
            # print(self.used)
            return self.cache_data.get(key)
