from lru_cache.LRUCache import LRUCache

"""
This file was used for debugging the LRUCache
"""

if __name__ == '__main__':
    
    lru = LRUCache(3)
    
    for i in range(0,3):
        lru.put(i, str(i)) 
    
    print(lru._printForward())

    lru.reset()

    lru.put(0, 'a')
    lru.put(1, 'b')
    lru.put(2, 'c')

    print(lru._printForward())

    lru.get(1)
    #lru.reset()

    lru.put(1, 'a')
    
    print(lru._printForward())
    print("-")

    lru.delete(2)

    print(lru._printForward())
    print("-")

    lru.delete(3)

    print(lru._printForward())
    print("-")

    lru.delete(1)
    print(lru._printForward())
    print("-")