def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 使用list.pop(0)时间复杂度是O(n)
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    m = len(arr) // 2
    # 使用切片的时间复杂度是O(k)
    return merge(merge_sort(arr[:m]), merge_sort(arr[m:]))
    
    
arr = [5,4,3,2,1]
print(merge_sort(arr))

print('*' * 100)

def merge2(arr, l, m, r):
    pass
    
    
def merge_sort2(arr, l, r):
    if l < r:
        m = (l + r) // 2
        
        merge_sort2(arr, l, m)
        merge_sort2(arr, m+1, r)
        merge2(arr, l, m, r)
    

    
    
    
