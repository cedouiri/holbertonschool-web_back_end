#!/usr/bin/env python3
'''
Simple helper function

'''

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list:
        '''
        return inner list
        '''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        indexes = index_range(page, page_size)
        try:
            return self.dataset()[indexes[0]:indexes[1]]
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> tuple:
    '''
    a function named index_range that takes two integer
    arguments page and page_size
    '''
    p = page * page_size - page_size
    return (p, p + page_size)
