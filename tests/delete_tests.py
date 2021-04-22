from lru_cache.LRUCache import LRUCache
import pytest

"""
Tests the delete operations of the LRU Cache
"""

def test_delete_1():
    """
    Tests that an item can be removed from the cache
    Delete from middle
    """
    lru = LRUCache(5)

    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)

    lru.delete(2)

    assert lru._printForward() == [1, 3]

def test_delete_2():
    """
    Tests that an item can be removed from the cache
    Delete from head
    """
    lru = LRUCache(5)

    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)

    lru.delete(1)

    assert lru._printForward() == [2, 3]

def test_delete_3():
    """
    Tests that an item can be removed from the cache
    Delete from tail
    """
    lru = LRUCache(5)

    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)

    lru.delete(3)

    assert lru._printForward() == [1, 2]

def test_delete_4():
    """
    Tests deletting a key that doesn't exist results in a no-op
    """
    lru = LRUCache(5)

    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)

    lru.delete(10)

    assert lru._printForward() == [1, 2, 3]