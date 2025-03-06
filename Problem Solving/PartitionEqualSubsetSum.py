def isEqualSubset(nums):
    total = sum(nums)
    if total % 2 != 0: 
        return False
    else: 
        target = total // 2
    dp = set()
    dp.add(0)
    for i in range(len(nums)-1, -1, -1):
        temp_dp = dp
        for val in dp: 
            if val + nums[i] == target:
                return True 
            temp_dp.add(val + nums[i])
        dp = temp_dp 
        
    return True if target in dp else False 
    
arr = [1, 2, 3, 4, 5, 6, 7, 28]
result = isEqualSubset(arr)
if result: 
    print("The Given Array can be partitioned with Equal Subset Sum")
else:
    print("The Given Array cannot be partitioned with Equal Subset Sum")
