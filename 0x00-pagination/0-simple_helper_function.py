#!/usr/bin/env python3
""" Module for the index_range function """


def index_range(page, page_size):
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
