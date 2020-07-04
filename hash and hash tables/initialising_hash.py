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

#--------------------------------------------------------------------------------------------------------------
#  Hash table collision handling implementation in python
# case of collision where value of March 17 is displayed by March 6 as generated hashes are same

class HashTable:
    
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h%self.MAX    
            
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in  self.arr[h]:
            if element[0] == key:
                return element[1]
        
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
        
        
    def __delitem__(self, key): 
        h = self.get_hash(key)
        for inx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][inx]
        
        
H = HashTable()

H['March 1'] = '120'
H['March 2'] = '12'
H['March 3'] = '1'
H['March 4'] = '180'
H['March 5'] = '18'
H['March 6'] = '0'
H['March 17'] = '1200'
print(H.arr)
print(H.get_hash('March 17'))
print(H.get_hash('March 6'))
del H['March 1']
del H['March 17']
print(H.arr)

    
    
