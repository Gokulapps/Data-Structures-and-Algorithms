def bubble_sort(arr):  
    n = len(arr)  
    # Traverse through all array elements  
    for i in range(n):  
        # Set a flag to detect any swap  
        swapped = False  
        # Ignoring Last i elements as they will be in sorted order
        for j in range(0, n - i - 1):  
            # Compare each pair of adjacent items  
            if arr[j] > arr[j + 1]:  
                # Swap if elements are in the wrong order  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True  
        # If no elements were swapped in the inner loop, then the list is sorted  
        if not swapped:  
            break  
  
# Example usage:  
my_list = [64, 34, 25, 12, 22, 11, 90]  
print("Original array:")  
print(my_list)  
  
bubble_sort(my_list)  
print("\nSorted array:")  
print(my_list)  
