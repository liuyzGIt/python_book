def binary_search(alist, item):
    front = 0
    rear = len(alist) - 1
    
    found = False
    while front <= rear and not found:
            mid = (rear + front) // 2
            if alist[mid] > item:
                rear = mid - 1
            elif alist[mid] < item:
                front = mid + 1
            else:
                found = True
    return found
    
# print(binary_search([0,1,2,3,4,5,6,7,8,9,10], 100))


def binary_search_recursion(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = (len(alist) - 1) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search_recursion(alist[:mid], item)
        elif alist[mid] < item:
            return binary_search_recursion(alist[mid+1:], item)

            
# for i in [0,1,2,3,4,5,6,7,8,9,10,100]:    
    # print(i, binary_search([0,1,2,3,4,5,6,7,8,9,10], i))
    
    
def binary_search_recursion_without_slice(alist, start, end, item):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search_recursion_without_slice(alist, start, mid-1, item)
        elif alist[mid] < item:
            return binary_search_recursion_without_slice(alist, mid+1, end, item)

alist = [0,1,2,3,4,5,6,7,8,9,10,100]
for i in alist:    
    print(i, binary_search_recursion_without_slice(alist,0,len(alist)-1, i))
    
print(binary_search_recursion_without_slice(alist,0,len(alist)-1, 200))
