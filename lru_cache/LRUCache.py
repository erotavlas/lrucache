import lru_cache.Node as Node

class LRUCache:
    """
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
    """
    def __init__(self, maxsize):
        self.maxsize = maxsize # number of max items
        self.currentsize = 0 # holds current items in cache

        self.dictionary = {} # stores nodes by key

        self.head = None # least recent request (oldest)
        self.tail = None # most recent request (newest)


    def put(self, key, value):
        """
        Adds a value to the lru cache.   
        If there is space available - the item is appended to the end
        If the cache is full - the least recently used item is removed to make room for the new item
        """

        if key in self.dictionary:
            # key exists - move to end of list only if not already at the end
            # i.e. make most recent 
            self._makeRecentlyUsed(key)
        else:
            if self.currentsize != self.maxsize:
                
                # this is most recent - append to end
                self._append(key, value)

            else:
                # cache is full
                # remove the least recently used
                leastRecentlyUsed = self.head
                self.delete(leastRecentlyUsed.key)

                # append to end
                self._append(key, value)

    def get(self, key):
        """
        Gets the value for a key in the cache
        """
        value = -1
        if key in self.dictionary:
            node = self.dictionary[key]
            value = node.value

            if node.nextNode != None: # not the tail
                self._makeRecentlyUsed(key)
        
        return value
    
    def delete(self, key):
        """
        Delete a key
        """
        if key in self.dictionary:
            node = self.dictionary.pop(key)
            self.currentsize -= 1

            if node.nextNode == None and node.prevNode != None: # last node
                prevNode = node.prevNode
                prevNode.nextNode = None
                self.tail = prevNode
            
            elif node.prevNode == None and node.nextNode != None: # first node
                nextNode = node.nextNode
                nextNode.prevNode = None
                self.head = nextNode

            elif node.prevNode != None and node.nextNode != None:
                node.prevNode.nextNode = node.nextNode
                node.nextNode.prevNode = node.prevNode

            elif node.prevNode == None and node.nextNode == None: # only one node
                self.head = None
                self.tail = None


    def reset(self):
        """Clears the cache"""
        if self.currentsize > 0:
            currentNode = self.head
            while currentNode != None:
                nextNode = currentNode.nextNode
                currentNode.nextNode = None
                currentNode.prevNode = None
                currentNode.value = None
                currentNode = nextNode
            
            self.head = None
            self.tail = None
            self.dictionary.clear()
            self.currentsize = 0

    def _append(self, key, value):
        """
        Appends a node to the end of the lru cache making it the 
        most recently used item.
        """
        node = Node.ListNode(key, value)

        #there are no values in the linked list
        #make this node the head node and return
        if self.head is None:
            self.head = node
            self.tail = node
            self.dictionary[key] = node
            self.currentsize += 1
            return

        lastNode = self.tail
        lastNode.nextNode = node
        node.prevNode = lastNode
        self.tail = node

        self.dictionary[node.key] = node
        self.currentsize += 1

    def _makeRecentlyUsed(self, key):
        """
        Makes a node recently used by moving it to the end of the cache
        """
        node = self.dictionary[key]

        if node.nextNode != None: # not the tail
            if node.prevNode == None and node.nextNode != None: # head node before another node
                nextNode = node.nextNode
                nextNode.prevNode = None
                self.head = nextNode
            elif node.prevNode != None and node.nextNode != None: # in between nodes
                node.prevNode.nextNode = node.nextNode
                node.nextNode.prevNode = node.prevNode

            # place after last node - make it the tail 
            lastNode = self.tail
            lastNode.nextNode = node
            node.prevNode = lastNode
            node.nextNode = None
            self.tail = node


    def _printForward(self):
        """
        Helper function - return contents of cache, forward direction
        """
        contents = []
        node = self.head

        while (node != None):
            contents.append(node.value)
            node = node.nextNode
        
        return contents
    
    def _printReverse(self):
        """
        Helper function - return contents of cache, reverse direction
        """
        node = self.tail
        contents = []

        while (node != None):
            contents.append(node.value)
            node = node.prevNode

        return contents


