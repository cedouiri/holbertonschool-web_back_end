#!/usr/bin/python3

'''
Basic dictionary


'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    a class BasicCache that inherits from BaseCaching

    '''

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything
        '''

        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None
        '''

        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
