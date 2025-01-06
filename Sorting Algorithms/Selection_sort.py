def selection_sort(arr):  
    n = len(arr)  
    # Traverse through all array elements  
    for i in range(n):  
        # Find the minimum element in remaining unsorted array  
        min_idx = i  
        for j in range(i + 1, n):  
            if arr[j] < arr[min_idx]:  
                min_idx = j  
        # Swap the found minimum element with the first element  
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  
  
# Example usage:  
my_list = [64, 25, 12, 22, 11]  
print("Original array:")  
print(my_list)  
  
selection_sort(my_list)  
print("\nSorted array:")  
print(my_list)  
