#!/usr/bin/python3

'''
Basic dictionary


'''

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''
    a class LFUCache that inherits from BaseCaching

    '''

    def __init__(self):

        self.usedKey = {}
        self.timesKey = {}
        self.time = 0
        super().__init__()

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything
        '''

        if key is not None and item is not None:
            if key not in self.usedKey:
                self.usedKey[key] = 1
            else:
                self.usedKey[key] += 1
            self.timesKey[key] = self.time
            self.time += 1
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            cpyusedKey = self.usedKey.copy()
            del cpyusedKey[key]
            smallest_value = min(cpyusedKey, key=cpyusedKey.get)
            smallest_value = cpyusedKey[smallest_value]
            sameKeyValue = {}
            for _key, _value in cpyusedKey.items():
                if _value == smallest_value:
                    sameKeyValue[_key] = _value
            if len(sameKeyValue) == 1:
                discard_key = list(sameKeyValue.keys())[0]
            else:
                time_sameKeyValue = {}
                for _key, _value in self.timesKey.items():
                    if _key in sameKeyValue:
                        time_sameKeyValue[_key] = _value

                discard_key = min(time_sameKeyValue, key=time_sameKeyValue.get)
            del self.cache_data[discard_key]
            del self.usedKey[discard_key]
            del self.timesKey[discard_key]

            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        '''
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in
        self.cache_data, return None
        '''

        if key is None or key not in self.cache_data:
            return None
        self.usedKey[key] += 1
        self.timesKey[key] = self.time
        self.time += 1
        return self.cache_data[key]
