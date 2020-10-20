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


if __name__ == "__main__":
    e = SelectionSort([5,4,3,2,1])
    e.sort()
    print(e.show())
