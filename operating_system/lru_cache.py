
# we return the value of the key that is queried in O(1) and return -1 if we don't find the key in out dict / cache. 
# And also move the key to the end to show that it was recently used.
# first, we add / update the key by conventional methods. 
# But here we will also check whether the length of our ordered dictionary has exceeded our capacity, If so we remove the first key (least recently used) 

from collections import OrderedDict 
  
class LRUCache: 
    def __init__(self, capacity: int): 
        self.cache = OrderedDict() 
        self.capacity = capacity 
   
    def get(self, key: int) -> int: 
        if key not in self.cache: 
            return -1
        else: 
            # move_to_end() method is used to efficiently reposition an element to an endpoint.
            self.cache.move_to_end(key) 
            return self.cache[key] 
  
    def put(self, key: int, value: int) -> None: 
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False) 
  
# Initialized LRUCashe as main
c = int(input())
main = LRUCache(c)  
cache.put(1, 1) 
print(main.cache) 
cache.put(2, 2) 
print(main.cache) 
cache.get(1) 
print(main.cache) 
cache.put(3, 3) 
print(main.cache) 
cache.get(2) 
print(main.cache) 
cache.put(4, 4) 
print(main.cache) 
cache.get(1) 
print(main.cache) 
cache.get(3) 
print(main.cache) 
cache.get(4) 
print(main.cache) 
