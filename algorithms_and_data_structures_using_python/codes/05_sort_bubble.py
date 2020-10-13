def bubblesort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    
def shotbubblesort(alist):
    n = len(alist)
    for i in range(n):
        exchange = False
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        print(exchange)
        if not exchange:
            return
             
alist = [5,4,3,2,1,10,90,33,54,79,152]
shotbubblesort(alist)
print(alist)
                
