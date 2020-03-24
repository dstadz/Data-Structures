from doubly_linked_list import DoublyLinkedList, ListNode



class LRUCache:
    """
    Our LRUCache class keeps track of
    -the max number of nodes it can hold,
    -the current number of nodes it is holding,
    -a doubly-linked list that holds the key-value entries in the correct order,
    -as well as a storage dict that provides fast access to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.list = DoublyLinkedList()
        self.storage = {}



    """
    Retrieves the value associated with the given key.
    Also needs to move the key-value pair to the end of the order such that the pair is considered most-recently used.
    if the key-value pair doesn't exist in the cache
        Return the value associated with the key or None
    """
    def get(self, key):
        print('get',key, self.storage)
        if key in self.storage.keys():
            node = ListNode({key, self.storage[key]})
            self.list.remove_from_head()
            self.list.add_to_tail(node)
            return self.storage[key]
        else:
            return None

    """
    Adds the given key-value pair to the cache.
    The newly-added pair should be considered the most-recently used entry in the cache.
    If the cache is already at max capacity before this entry is added,
        then the oldest entry in the cache needs to be removed to make room.
    Additionally, in the case that the key already exists in the cache,
        we simply want to overwrite the old value associated with the key with the newly-specified value.
    """
    def set(self, key, value):
        print('set', key,value, self.storage)
        node = ListNode({key:value})
        if key in self.storage.keys():
            self.storage[key] = value
            self.list.add_to_tail(node)
        elif self.size == self.limit:
            self.storage[key] = value
            old = self.list.remove_from_head()
            self.storage.pop(next(iter(old.value)), None)
            self.list.add_to_tail(node)
        else:
            self.size += 1
            self.storage[key] = value
            self.list.add_to_tail(node)
