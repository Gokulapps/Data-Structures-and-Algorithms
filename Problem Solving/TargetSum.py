def targetSumWays(nums, target):
    last_index = len(nums)
    cache = {}
    def dfs(index, total):
        if index == last_index: 
            return 1 if total == target else 0 
        if (index, total) in cache:
            return cache[(index, total)]
        cache[(index, total)] = dfs(index+1, total+nums[index]) + dfs(index+1, total-nums[index])
        return cache[(index, total)]
      
    return dfs(0, 0)
    
nums = [1, 1, 1, 1, 1]
target = 3 
totalWays = targetSumWays(nums, target)
print("Total Number of Ways to arrive at the Target is:", totalWays)
