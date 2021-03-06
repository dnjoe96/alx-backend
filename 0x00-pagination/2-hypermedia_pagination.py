#!/usr/bin/env python3
""" Module for the Server function """
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """ The function returns the range for a page
    Args:
        page: int - The page of interest
        page_size: int - The size of a page
    Return:
        Tuple of start and end index of a range for a page
    """
    pages = page * page_size
    end_index = pages
    start_index = pages - page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        # self.DATA_FILE = Server.DATA_FILE

    def dataset(self) -> List[List]:
        """ Cached dataset
        """
        if self.__dataset is None:
            # print(self.DATA_FILE)
            # print('ghto here')
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                # print(dataset)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Get a page based on given range """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        start, end = index_range(page, page_size)
        if end > len(self.DATA_FILE):
            return []
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Hypermedia generator """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        if self.__dataset:
            size = len(self.__dataset)
        else:
            size = 0
        dic = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page + 1 <= size else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(size / page_size),
        }
        return dic
