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
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LCList:
    def __init__(self):
        self.rear = None  # 只要一个尾指针
        
    def is_empty(self):
        return self.rear is None
        
    def prepend(self, data):
        """前端插入"""
        p = Node(data)
        if self.rear == None:
            p.next = p
            self.rear = p
        else:
            p.next = self.rear.next
            self.rear.next = p
            
    def append(self, data):
        self.prepend(data)
        self.rear = self.rear.next
        
        
    def pop(self): # 前端出栈
        if self.is_empty():
            raise ValueError('empty in pop')
        p = self.rear.next
        if self.rear is p:
            self.rear = None
        else:
            self.rear.next = p.next
        return p.data
        
class Josephus(LCList):
    def __init__(self, n, k, m):
        super().__init__()
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop())
    
        
    def turn(self, m):
        for i in range(m):
            self.rear = self.rear.next
    
    
                
        
Josephus(10, 3, 7)       
        
    
    
 
print('-' * 100)

for i in josephus_queue(10, 3, 7):
    print(i)
    

# for i in josephus_list_2(10, 3, 7):
    # print(i)
    
    
    
