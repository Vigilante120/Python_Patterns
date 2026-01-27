from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        value = self.cache.pop(key)
        self.cache[key]=value
        return value
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Update value and move to end
            self.cache.pop(key)
        self.cache[key] = value
        
        # Remove least recently used (first item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
