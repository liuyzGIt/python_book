def shell_sort(arr):
    n = len(arr)
    gap = n //2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
                
            arr[j] = temp
            print(arr)
        
        gap = gap // 2
            
                     
            
            
    
    
arr = [10,9,8,7,6,5,4,3,2,1,0]
shell_sort(arr)
print(arr)
