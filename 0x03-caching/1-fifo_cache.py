#!/usr/bin/python3

'''
Basic dictionary


'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    a class FIFOCache that inherits from BaseCaching

    '''

    def __init__(self):

        super().__init__()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything
        '''

        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                first = sorted(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(first))
                del self.cache_data[first]
                self.cache_data[key] = item
            else:
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
