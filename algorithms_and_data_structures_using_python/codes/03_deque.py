class Deque:
    
    def __init__(self):
        self.elems = []
    
    def is_empty(self):
        return not self.elems
        
    def size(self):
        return len(self.elems)
        
    def add_front(self, item):
        self.elems.insert(0, item)
        
    def add_rear(self, item):
        self.elems.append(item)
        
    def remove_front(self):
        if self.is_empty():
            raise ValueError('queue empty in reomve front')
        return self.elems.pop(0)
        
            
    def remove_rear(self):
        if self.is_empty():
            raise ValueError('queue empty in reomve rear')
        return self.elems.pop()
        
    def __str__(self):
        return str(self.elems) + str(len(self.elems))



def palchecker(word):
    dq = Deque()
    for char in word:
        dq.add_front(char)
    still_equal = True
    while dq.size() > 1 and still_equal:
        f = dq.remove_front()
        r = dq.remove_rear()
        if f != r:
            still_equal = False
    
    return still_equal
    
    

def palchecker2(word):
    w = list(word)
    w.reverse()
    
    for i in range(len(w)):
        if w[i] != word[i]:
            return False
    return True
    
    
        
print(palchecker2('上海自来水来自海上'))
print(palchecker2('toot'))
print(palchecker2('aabbaad'))
