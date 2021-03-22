#!/usr/bin/python3

'''
Basic dictionary


'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''
    a class MRUCache that inherits from BaseCaching

    '''

    def __init__(self):

        super().__init__()
        self.ordered_cache_keys = []

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
                mru = self.ordered_cache_keys[-1]
                print('DISCARD: {}'.format(mru))
                self.ordered_cache_keys.remove(mru)
                self.ordered_cache_keys.append(key)
                del self.cache_data[mru]
                self.cache_data[key] = item
            elif (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key in self.cache_data.keys())
            ):
                self.ordered_cache_keys.remove(key)
                self.ordered_cache_keys.append(key)
                self.cache_data[key] = item
            else:
                self.ordered_cache_keys.append(key)
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
            self.ordered_cache_keys.remove(key)
            self.ordered_cache_keys.append(key)
            return self.cache_data[key]
