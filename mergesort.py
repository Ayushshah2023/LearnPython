def mergesort(arr):
    mid=int(len(arr)/2)
    Left=arr[:mid]
    Right=arr[mid:]
    for x in range(len(Left)): 
        print(Left[x])
    for x in range(len(Right)): 
        print(Right[x])
    Left.sort()
    Right.sort()
    i=j=k=0
    while i < len(Left) and j < len(Right): 
        if Left[i] < Right[j]: 
            arr[k] = Left[i] 
            i+=1
        else: 
            arr[k] = Right[j] 
            j+=1
        k+=1 
    if(i<len(Left)): 
        arr[k] = Left[i] 
        i+=1
        k+=1  
    if(j<len(Right)): 
        arr[k] = Right[j] 
        j+=1
        k+=1
    return(arr)
#print(mergesort([38,27,43,3,9,82,10]))
print(mergesort([1,22,44,55,22,99,66,77]))
#O(n^3) Solution 
