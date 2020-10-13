def selection_sort(alist):
    n = len(alist) 
    for i in range(n):
        pos_max = i
        for j in range(i+1, n):
            if alist[pos_max] > alist[j]:
                pos_max = j
        if i != pos_max:
            alist[pos_max], alist[i] =  alist[i], alist[pos_max]
            
            
             
alist = [5,4,3,2,1,10,90,33,54,79,152]
selection_sort(alist)
print(alist)
             
