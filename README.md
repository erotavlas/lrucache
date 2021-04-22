  ### Description
  
  Least Recently Used (LRU) Cache Implementation in Python
  The LRU Cache is initialized with a maximum size.  During use, if the
  max size is exceeded when adding new keys, the least recently used
  item is discarded from the cache to make room for the new item.

  Assumptions:
  - Minimum size = 1
  - Maximum size = any integer greater than 1
  - Get() operation return -1 if key not present in cache
  - Get() and Put() operation on an item that exists in the cache causes 
    the item to become the most recently used item (moves to tail of list)

  This LRU Cache is implemented as a doubly linked list where the least 
  recently used item is at the head of the list, and the most recently used
  item is at the tail of the list.
  
  ### Requirements
  
  Python 3 environment
  
  For running unit tests install `pytest` package to the environment.
  
  ### Usage
  
  Import into your project with 
  
  ```
  from lru_cache.LRUCache import LRUCache
  ```
  
  Initialize LRU Cache with a maximum size
  ```
  maxsize = 5
  lru = LRUCache(maxsize)
  ```
  
  Operations available
  
  NOTE:   
  
  `key` should be any a unique identifier of type such as string or int 
  
  `value` can be any object or custom type
  
  #### put(key, value)
  Put an item into the cache.  
  If item already exists, item is made most recently used.
  If item doesn't exists and there is space available in the cache, item is appended as
  most recently used.  If capacity of cache is exceeded, least recently used item is evicted
  and new item is appended as most recently used.
  ```
  lru.put(key, value)
  ```
  
  #### get(key) -> value
  Gets an item from the cache by key. 
  If the key doesn't exist in the cache, -1 is returned.
  If the item already exists in the cache, the item is returned and it is made most recently used.
  ```
  value = lru.get(key)
  ```
  
  #### delete(key)
  Removes an item from the cache by key.  
  If key doesn't exist in the cache, no action is performed.
  ```
  lru.delete(key)
  ```
  
  #### reset()
  Clears the cache.  All items will be removed.
  ```
  lru.reset()
  ```

  
