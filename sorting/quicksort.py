def partition(arr, low, high):
    pivot = arr[high]
    
    i = low 
    
    for j in range(low, high):
        if arr[j] <= pivot:
        
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    
    
    arr[i], arr[high] = arr[high], arr[i]
    return i
    
def quickSort(arr, low, high):
    
    if low<high:
        
        pi = partition(arr, low, high)
        
        quickSort(arr, pi+1, high)
        quickSort(arr, low, pi-1)
    


data = [1,4,2,5,3,2,4,6,7,55,32,]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
     
