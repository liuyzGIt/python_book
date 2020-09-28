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

# n个人从k开始报数，数到m的人退出


def josephus_queue(n, k, m):
    q = Queue()
    for i in range(n):
        q.enqueue(i+1)
        
    for i in range(k-1):
        q.enqueue(q.dequeue())
        
        
    while not q.is_empty():
        for i in range(m-1):
            q.enqueue(q.dequeue())
            
            
        yield q.dequeue()
        
        
def josephus_list(n, k, m):
    
    persons = list(range(1, n+1))
    pos = k - 1
    
    
    for time in range(n):
        count = 0
        while count != m:         
            if persons[pos] != 0:
               count += 1
            if count == m:
                person = persons[pos]
                persons[pos] = 0
                yield person
            pos = (pos+1) % n
            

def josephus_list_2(n, k, m):
    
    persons = list(range(1, n+1))
    pos = k - 1
    
    
    for num in range(n, 0, -1):
        pos = (pos + m -1) % num
        yield persons.pop(pos)
       

for i in josephus_queue(10, 3, 7):
    print(i)
    

for i in josephus_list_2(10, 3, 7):
    print(i)
    
    
    
