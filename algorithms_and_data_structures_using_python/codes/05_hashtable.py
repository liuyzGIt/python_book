class HashTable1:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
    def put(self, key, value):
        hashcode = self.hash_func(key)
        # 不存在key,添加
        if self.keys[hashcode] == None:
            self.keys[hashcode] = key
            self.values[hashcode] = value
        # 存在key,修改
        elif self.keys[hashcode] == key:
            self.values[hashcode] = value
        else:            
            old_hash = hashcode
            is_full = False
            is_added = False
            while not is_full and not is_added:                
                new_hash = self.rehash(old_hash)
                if new_hash == hashcode:
                    is_full = True
                # 不存在key,添加
                elif self.keys[new_hash] == None:
                    self.keys[new_hash] = key
                    self.values[new_hash] = value
                    is_added = True
                # 存在key,修改
                elif self.keys[new_hash] == key:
                    self.values[new_hash] = value
                    is_added = True
                else:
                    old_hash = new_hash
            if is_full:
                self.extend()
                self.put(key, value)
           
    def get(self, key):
        hashcode = self.hash_func(key)
        if self.keys[hashcode] == key:
            return self.values[hashcode]
        else:            
            old_hash = hashcode
            new_hash = self.rehash(old_hash)
            found = False
            while not found and old_hash != new_hash:                
                if self.keys[new_hash] == key:
                    return self.values[new_hash] 
                else:
                    new_hash = self.rehash(new_hash)

        
    def delete(self, key):
        hashcode = self.hash_func(key)
        if self.keys[hashcode] == key:
            self.keys[hashcode] = None
            self.values[hashcode] = None
        else:            
            old_hash = hashcode
            new_hash = self.rehash(old_hash)
            found = False
            while not found and old_hash != new_hash:                
                if self.keys[new_hash] == key:
                    self.keys[hashcode] = None
                    self.values[hashcode] = None 
                else:
                    new_hash = self.rehash(new_hash)
        
        
    def length(self):
        return len([x for x in self.keys if x is not None])
        
    def hash_func(self, key):
        return key % self.size
        
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size
        
    def extend(self):
        old_keys = self.keys
        old_values = self.values
                
        self.size = self.size * 2
        self.keys = [None] * self.size
        self.values = [None] * self.size
        
        for i in range(len(old_keys)):
            self.put(old_keys[i], old_values[i])
            
    def show(self):
        print(self.keys, self.values)
        

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
    def __str__(self):
        return '({0}, {1})'.format(self.key, self.value)
        
        

class HashTable2:
    def __init__(self, size=11):
        self.size = size 
        self.slots = [None] * self.size
        
    def put(self, key, value):
        hashcode = self.hash_func(key)
        if self.slots[hashcode] == None:
            self.slots[hashcode] = HashItem(key, value)
        else:
            item = self.slots[hashcode]
            while item is not None:
                if item.key == key:
                    item.value = value
                elif item.next is not None:
                    item = item.next
                else:
                    item.next = HashItem(key, value)
                    break
                    
        
    def get(self, key):
        pass
        
    def contains(self, key):
        pass
        
    def delete(self, key):
        pass
        
    def length(self):
        pass
        
    def show(self):
        for index, item in enumerate(self.slots):
            print(index, end= ": ")
            value = item
            while value is not None:
                print(value, end=" ")
                value = value.next
            print()
            
        
    def hash_func(self, key):
        return key % self.size
        
if __name__ == "__main__":
    # ht = HashTable1()
    # ht.put(1, 1)
    # ht.put(11, 1)
    # ht.put(12, 1)
    # ht.put(23, 1)
    # ht.put(34, 1)
    # ht.show()
    # print(ht.length())
    # ht.delete(1)
    # print(ht.length())
    # ht.put(1,3)
    # ht.show()
    
    ht2 = HashTable2()
    ht2.put(1,1)
    ht2.put(12,12)
    ht2.show()
    
    
