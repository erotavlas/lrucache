    Least Recently Used (LRU) Cache Implementation in Python
    The LRU Cache is initialized with a macimum size.  During use, if the
    max size is exceeded when adding new keys, the least recently used
    item is discarded form the cache to make room for the new item.

    Assumptions:
    - Minimum size = 1
    - Maximum size = any integer greater than 1
    - Get() operation return -1 if key not present in cache
    - Get() and Put() operation on an item that exists in the cache causes 
      the item to become the most recently used item (moves to tail of list)

    This LRU Cache is implemented as a doubly linked list where the least 
    recently used item is at the head of the list, and the most recently used
    item is at the tail of the list.