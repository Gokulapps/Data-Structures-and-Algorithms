def quick_sort(arr):  
    if len(arr) <= 1:  
        return arr  # If the len(arr) is less than 1 it returns the array
    else:  
        pivot = arr[0]  # First element is taken as pivot element
        less_than_pivot = [element for element in arr[1:] if element <= pivot]  # list having elements lsmaller than pivot
        greater_than_pivot = [element for element in arr[1:] if element > pivot]  # list having elements greater than pivot
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)  
  
# Example
arr = [3,6,8,10,1,2,1]  
print(quick_sort(arr))  
