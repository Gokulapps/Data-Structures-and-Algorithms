# Algorithm 1 - Dynamic Programming 
def computeLIS(arr):
    arr_len = len(arr)
    LIS = [1] * arr_len
    for i in range(arr_len, -1, -1):
        for j in range(i+1, arr_len): 
            if arr[i] < arr[j]: 
                LIS[i] = max(LIS[i], 1+LIS[j])
    return max(LIS)
    
arr = [1, 3, 4, 2, 0, 9, 8]
result = computeLIS(arr)
print(f"Longest Increasing Subsequence in the given Array is: {result}")
