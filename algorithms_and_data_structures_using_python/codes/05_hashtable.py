class HashTable1:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def put(self, key, value):
        hashcode = self.hash(key)
        if self.keys[hashcode] == None：
            self.keys[hashcode] = key：
            self.values[hashcode] = value
        elif self.keys[hashcode] == key:
            self.values[hashcode] = value
        else:
            
            
        
    def get(self, key):
        pass
        
    def delete(self, key):
        pass
        
    def length(self):
        pass
        
    def hash(self, key):
        return key % self.size
        
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size
        
    def extend(self)：
        self.size = self.size * 2
        new_keys = [None] * new_size
        new_values = [None] * new_size
    
