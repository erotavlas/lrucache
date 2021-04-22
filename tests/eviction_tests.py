from lru_cache.LRUCache import LRUCache
import pytest

"""
These tests check the Least Recently Used property is obeyed
when the cache size has reached capacity
i.e. Put function on keys present in the cache cause the
least recently used item to be evicted from the cache and the new 
item appended to the end
"""

def test_put_1():
    """Put new item, head of list is evicted"""
    lru = LRUCache(5)
    
    for i in range(0,5):
        lru.put(i, i) 

    lru.put(20, 20)

    assert lru._printForward() == [1,2, 3, 4, 20] 

def test_put_2():
    """Put an item that already exists, no evictions"""
    lru = LRUCache(5)
    
    for i in range(0,5):
        lru.put(i, i) 

    lru.put(0, 0)

    assert lru._printForward() == [1, 2, 3, 4, 0] 


def test_put_3():
    """Put new items, all previus items are eventually evicted"""
    lru = LRUCache(5)
    
    for i in range(0,5):
        lru.put(i, i) 

    for i in range(10,15):
        lru.put(i, i)    

    assert lru._printForward() == [10, 11, 12, 13, 14] 