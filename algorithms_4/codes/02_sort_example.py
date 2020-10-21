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
            
class SelectionSort2(Example):
    def sort(self):
        elems = self.elems
        for i in range(len(elems)):
            index = i
            for j in range(i+1, len(elems)):
                if(elems[j] < elems[index]):                   
                    index = j
            #self.exchange(i, index)
            elems[i], elems[index] = elems[index], elems[i]

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
            
class ShellSort(Example):
    def sort(self):
        elems = self.elems
        length = len(elems)
        h = length // 2        
        while h > 0:
            for i in range(h, length):
                # for j in range(i, h-1, -h):
                    # if self.less(self.elems[j], self.elems[j-h]):
                        # self.exchange(j, j-h) 
                # print(len(arr))
                temp =elems[i] 
                j = i 
                while  j >= h and elems[j-h] > temp: 
                    elems[j] = elems[j-h] 
                    j -= h 
                elems[j] = temp
            h = h // 2
        # arr = self.elems  
        # n = len(arr)
        # gap = int(n/2)  
        # while gap > 0:  
            # for i in range(gap,n): 
      
                # temp = arr[i] 
                # j = i 
                # while  j >= gap and arr[j-gap] >temp: 
                    # arr[j] = arr[j-gap] 
                    # j -= gap 
                # arr[j] = temp 
            # gap = int(gap/2)

class ShellSort2(Example):
    def sort(self):
        length = len(self.elems)
        h = 1
        while h < length//3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, length):
                for j in range(i, h-1, -h):
                    if self.less(self.elems[j], self.elems[j-h]):
                        self.exchange(j, j-h)            
            h = h // 3
        
class SS:
    def __init__(self, arr):
        self.arr = arr
    
    def shellSort(self):
        arr = self.arr  
        n = len(arr)
        gap = int(n/2)
      
        while gap > 0: 
      
            for i in range(gap,n): 
      
                temp = arr[i] 
                j = i 
                while  j >= gap and arr[j-gap] >temp: 
                    arr[j] = arr[j-gap] 
                    j -= gap 
                arr[j] = temp 
            gap = int(gap/2)
    
class SS2(Example):
    
    def sort(self):
        arr = self.elems  
        n = len(arr)
        gap = int(n/2)
      
        while gap > 0:       
            for i in range(gap,n):       
                temp = arr[i] 
                j = i 
                while  j >= gap and arr[j-gap] >temp: 
                    arr[j] = arr[j-gap] 
                    j -= gap 
                arr[j] = temp 
            gap = int(gap/2)


if __name__ == "__main__":
    # e = SelectionSort([5,4,3,2,1])
    # e = InsertSort([5,4,3,2,1,10,66,33,22,66])
    # e = InsertSort_my([5,4,3,2,1,10,66,33,22,66])
    # e = InsertSort2([5,4,3,2,1,10,66,33,22,66])
    # e.sort()
    # print(e.show())
    
    import timeit
    import random
    # arr = []
    # for i in range(10000):
        # arr.append(random.randint(0,100000))
    
    # print(len(arr))
    arr = [5,4,3,2,1,10,66,33,22]

    # ssort = SelectionSort(arr)
    # isort = InsertSort(arr)
    # isort_my = InsertSort_my(arr)
    # isort2 = InsertSort2(arr)
    # t1 = (timeit.timeit(stmt=ssort.sort, number=1))
    # t2 = (timeit.timeit(stmt=isort.sort, number=1))
    # t3 = (timeit.timeit(stmt=isort_my.sort, number=100000))
    # t4 = (timeit.timeit(stmt=isort2.sort, number=100000))
    # print(t1) # 1.75
    # print(t2) # 0.32
    # print(t3) # 1.5
    # print(t4) # 0.41
    
    # shell = ShellSort(arr)
    # shell.sort()
    # print(shell.show())
    # print(timeit.timeit(stmt=shell.sort, number=1))
    # ss = SS2(arr)
    # print(timeit.timeit(stmt=ss.sort, number=1))
    
    # def eq():
        # a,b=100,1000
        # a=100
    # def eq2():
        # a,b=100,1000
        # a,b=b,a
    
    # print(timeit.timeit(stmt=eq,  number=10000000))
    # print(timeit.timeit(stmt=eq2, number=10000000))
    
    s1 = SelectionSort(arr)
    s2 = SelectionSort2(arr)
    # print(s2.sort())
    # print(s2.show())
    print(timeit.timeit(stmt=s1.sort,  number=10000))
    print(timeit.timeit(stmt=s2.sort,  number=10000))
    
    class SORT:
        def __init__(self, arr):
            self.arr = arr
        def sort(self):
            A = self.arr
            for i in range(len(A)): 
          
       
                min_idx = i 
                for j in range(i+1, len(A)): 
                    if A[min_idx] > A[j]: 
                        min_idx = j 
                            
                A[i], A[min_idx] = A[min_idx], A[i] 
    a = SORT(arr)
    print(timeit.timeit(stmt=a.sort,  number=10000))
    
    
