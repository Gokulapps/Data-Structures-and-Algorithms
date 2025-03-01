# Algorithm 1 - Brute Force Solution (Exploring all possible Sub Arrays)
def maxProduct(nums) -> int:
    res = nums[0]

    for i in range(len(nums)):
        cur = nums[i]
        res = max(res, cur)
        for j in range(i + 1, len(nums)):
            cur *= nums[j]
            res = max(res, cur)
            
    return res
    
array = [1, 2, 3, 4, 5, 6, 0, 2, 4, 5, 10]
maxProd = maxProduct(array)
print('The Maximum Product of the Sub Array is: ', maxProd)

# Algorithm 2 - Efficient Solution using Dynamic Programming 
def maxProductSubArray(array):
    currMax, currMin = 1, 1
    res = max(array)
    for num in array:
        temp = num * currMax
        currMax = max(temp, num * currMin, num)
        currMin = min(temp, num * currMin, num)
        res = max(res, currMax)
    
    return res 
    
array = [1, 2, 3, 4, 5, 6, 0, 2, 4, 5, 10]
maxProd = maxProductSubArray(array)
print('The Maximum Product of the Sub Array is: ', maxProd)
