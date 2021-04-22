from lru_cache.LRUCache import LRUCache
import pytest

"""
These tests check the consistency of the cache size
i.e. current size reported is consistent with the operations that 
have been performed
"""

def test_initialized():
    """A new LRUCache should have size 0"""
    lru = LRUCache(100)

    assert lru.currentsize == 0

def test_put_1():
    """Put one item => size == 1"""
    lru = LRUCache(1)

    lru.put(1,'a')

    assert lru.currentsize == 1

def test_put_2():
    """Put two different items, max size 1 => size == 1"""
    lru = LRUCache(1)

    lru.put(1,'a')
    lru.put(2,'b')

    assert lru.currentsize == 1

def test_put_3():
    """Put one item, then delete, max size 1 => size == 0"""
    lru = LRUCache(1)

    lru.put(1,'a')
    lru.delete(1)

    assert lru.currentsize == 0

def test_put_4():
    """Put 5 item, max size 10 => size == 5"""
    lru = LRUCache(10)

    lru.put(1,'a')
    lru.put(2,'b')
    lru.put(3,'c')
    lru.put(4,'d')
    lru.put(5,'e')

    assert lru.currentsize == 5

def test_put_5():
    """Put 10 item, max size 10 => size == 10"""
    lru = LRUCache(10)

    for i in range(0,10):
        lru.put(i, str(i))

    assert lru.currentsize == 10

def test_put_6():
    """Put same item over and over, max size 10 => size == 1"""
    lru = LRUCache(10)

    for i in range(0,10):
        lru.put(0, str(0))

    assert lru.currentsize == 1

def test_put_7():
    """Put same item over and over, max size 10 => size == 1"""
    lru = LRUCache(10)

    for i in range(0,10):
        lru.put(0, str(0))

    assert lru.currentsize == 1

def test_reset():
    """Put some items in cache, then clear it => size == 0"""
    lru = LRUCache(10)

    for i in range(0,10):
        lru.put(i, str(i))

    lru.reset()

    assert lru.currentsize == 0

def test_get():
    """Get an item => size remains the same"""
    lru = LRUCache(10)

    for i in range(0,10):
        lru.put(i, str(i))

    val = lru.get(1)

    assert lru.currentsize == 10

def test_delete():
    """Add 10 items then delete 3 ==> size == 7"""
    lru = LRUCache(10)

    for i in range(0,10):
        lru.put(i, str(i))

    lru.delete(0)
    lru.delete(3)
    lru.delete(7)

    assert lru.currentsize == 7