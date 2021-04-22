from lru_cache.LRUCache import LRUCache
import pytest

"""
These tests check the Least Recently Used property is obeyed when the
cache size capacity hasn't yet been reached.
i.e. Put and Get functions on keys present in the cache cause the
cached item to become the most recently used item. No evictions should occur here.
"""

def test_put_1():
    """
    Put an item which exists in cache, causes it to become most recently used
    """
    lru = LRUCache(10)

    lru.put(1, str(1))
    lru.put(2, str(2))
    lru.put(3, str(3))

    lru.put(1, str(1))

    assert lru._printForward() == ['2', '3', '1']

def test_get_1():
    """
    Get least recently used item makes it most recently used
    """

    lru = LRUCache(10)

    lru.put(1, str(1))
    lru.put(2, str(2))
    lru.put(3, str(3))

    lru.get(1)

    assert lru._printForward() == ['2', '3', '1']

def test_get_2():
    """
    Getting the most recent item, cauess no change in its position
    """
    lru = LRUCache(10)

    lru.put(1, str(1))
    lru.put(2, str(2))
    lru.put(3, str(3))

    lru.get(3)

    assert lru._printForward() == ['1', '2', '3']

def test_get_3():
    """
    Getting item in middle of list, item becomes most recent
    """
    lru = LRUCache(10)

    lru.put(1, str(1))
    lru.put(2, str(2))
    lru.put(3, str(3))

    lru.get(2)

    assert lru._printForward() == ['1', '3', '2']

def test_get_4():
    """
    Getting a key that doesn't exists returns -1
    """
    lru = LRUCache(5)

    lru.put(1, str(1))
    lru.put(2, str(2))
    lru.put(3, str(3))

    result = lru.get(10)

    assert result == -1

def test_get_5():
    """
    Getting item by key returns the value of the key
    """
    lru = LRUCache(5)

    lru.put(1, str(1))
    lru.put(2, str(2))
    lru.put(3, str(3))

    value = lru.get(2)

    assert value == '2'