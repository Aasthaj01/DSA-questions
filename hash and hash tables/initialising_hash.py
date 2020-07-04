#  Hash table implementation in python

class HashTable:
    
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h%self.MAX    
            
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
        
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __delitem__(self, key): 
        h = self.get_hash(key)
        self.arr[h] = None
        
H = HashTable()
H['March 1'] = '120'
H['March 2'] = '12'
H['March 3'] = '1'
print(H['March 2'])
del H['March 1']
print(H.arr)
    
