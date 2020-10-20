class Example:
    def __init__(self, elems):
        self.elems = list(elems)
        
    def sort(self):
        pass
    
    def less(self, v, w):
        return v < w
    
    def exchange(self, i, j):
        self.elems[i], self.elems[j] = self.elems[j], self.elems[i]
        
    def show(self):
        return str(self.elems)
        
    def is_sorted(self):
        for i in range(len(self.elems)-1):
            if not self.less(self.elems[i], self.elems[i+1]):
                return False
        return True


class SelectionSort(Example):
    def sort(self):
        for i in range(len(self.elems)):
            index = i
            for j in range(i+1, len(self.elems)):
                if self.less(self.elems[j], self.elems[index]):                   
                    index = j
            self.exchange(i, index)
            

class InsertSort_my(Example):
    def sort(self):
        for i in range(1, len(self.elems)):
            value = self.elems[i]
            for j in range(i+1):
                if self.less(self.elems[i], self.elems[j]):                   
                    for k in range(i, j, -1):
                        self.elems[k] = self.elems[k-1]
                    break
            self.elems[j] = value
            
            
class InsertSort(Example):
    def sort(self):
        for i in range(1, len(self.elems)):
            j = i
            while j > 0 and self.less(self.elems[j], self.elems[j-1]):
                self.exchange(j, j-1)
                j -= 1
                    
                    
class InsertSort2(Example):
    def sort(self):
        for i in range(1, len(self.elems)):
            j = i-1
            value = self.elems[i]
            while j >= 0 and self.less(value, self.elems[j]):
                self.elems[j+1] = self.elems[j]
                j -= 1
            self.elems[j+1] = value


    

if __name__ == "__main__":
    # e = SelectionSort([5,4,3,2,1])
    # e = InsertSort([5,4,3,2,1,10,66,33,22,66])
    # e = InsertSort_my([5,4,3,2,1,10,66,33,22,66])
    # e = InsertSort2([5,4,3,2,1,10,66,33,22,66])
    # e.sort()
    # print(e.show())
    
    import timeit
    arr = [5,4,3,2,1,10,66,33,22]
    ssort = SelectionSort(arr)
    isort = InsertSort(arr)
    isort_my = InsertSort_my(arr)
    isort2 = InsertSort2(arr)
    t1 = (timeit.timeit(stmt=ssort.sort, number=100000))
    t2 = (timeit.timeit(stmt=isort.sort, number=100000))
    t3 = (timeit.timeit(stmt=isort_my.sort, number=100000))
    t4 = (timeit.timeit(stmt=isort2.sort, number=100000))
    print(t1) # 1.75
    print(t2) # 0.32
    print(t3) # 1.5
    print(t4) # 0.41
