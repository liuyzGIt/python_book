class Queue:
    def __init__(self, lst=[]):
        self.elems = list(lst)
        self.size = len(self.elems)
        
    def is_empty(self):
        return not self.elems
        
    def size(self):
        return self.size
        
    def enqueue(self, item):
        self.elems.append(item)
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise ValueError(' dequeue empty ')
        return self.elems.pop(0)
        
    def __str__(self):
        return str(self.elems)
    

if __name__ == "__main__":
    q = Queue([1,2,3])
    print(q.dequeue())
    print(q)
            
    
    
