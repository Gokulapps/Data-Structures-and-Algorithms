# Algorithm 1 - Iterative Solution without cache but ensuring that only unique combinations are considered
def coinComb(target, denominations):
    noCoins = len(denominations)
    noCombinations = 0
    stack = [(0, 0)]
    while stack: 
        coin_index, total_amount = stack.pop(0)
        if total_amount == target: 
            noCombinations += 1
        elif total_amount > target:
            continue 
        elif coin_index >= noCoins: 
            continue
        else: 
            stack.append((coin_index, total_amount + denominations[coin_index]))
            stack.append((coin_index + 1, total_amount))
    
    return noCombinations
denominations = [1, 3, 5, 10, 20]
amount = 5
totalWays = coinComb(amount, denominations)
print(f'There are {totalWays} ways to sum up to {amount} using the given denominations')

# Algorithm 2 - Recursion Solution with cache along with ensuring unique combinations
def coinComb(target, denominations):
    noCoins = len(denominations)
    cache = {}
    def dfs(coin_index, total_amount): 
        if total_amount == target: 
            return 1 
        elif total_amount > target: 
            return 0 
        elif coin_index >= noCoins: 
            return 0 
        elif (coin_index, total_amount) in cache:
            return cache[(coin_index, total_amount)]
        else:
            cache[(coin_index, total_amount)] = dfs(coin_index, total_amount + denominations[coin_index]) + dfs(coin_index + 1, total_amount)  
            
            return cache[(coin_index, total_amount)]  
            
    return dfs(0, 0)
    
denominations = [1, 3, 5, 10, 20]
amount = 500
totalWays = coinComb(amount, denominations)
print(f'There are {totalWays} ways to sum up to {amount} using the given denominations')

# Algorithm 3 - Dynamic Programming Solution 
def coinComb(target_amount, denominations):  
    dp = [[0 if j!=0 else 1 for j in range(target_amount + 1)] for i in range(len(denominations) + 1)]  
    dp[0] = [0] * (target_amount+1)   
    for c in range(1, len(denominations) + 1):  
        for a in range(1, target_amount + 1):  
            dp[c][a] = dp[c - 1][a]  
            if a - denominations[c - 1] >= 0:  
                dp[c][a] += dp[c][a - denominations[c - 1]]  
      
    return dp[len(denominations)][target_amount]  
  
amount = 50  
denominations = [1, 3, 5, 10, 50]
totalWays = coinComb(amount, denominations)  
print(f'There are {totalWays} ways to sum up to {amount} using the given denominations')

# Algorithm 4 - Dynamic Programming Solution with improved space complexity 
def coinComb(target, denominations):
    dp = [0 if i!=0 else 1 for i in range(target+1)] 
    for i in range(len(denominations)):
        temp_dp = [0 if i!=0 else 1 for i in range(target+1)] 
        for amount in range(1, target+1):
            temp_dp[amount] = dp[amount]
            if amount - denominations[i] >= 0:
                temp_dp[amount] += temp_dp[amount - denominations[i]]
        dp = temp_dp
        
    return dp[target]  
  
amount = 50  
denominations = [1, 3, 5, 10, 50]
totalWays = coinComb(amount, denominations)  
print(f'There are {totalWays} ways to sum up to {amount} using the given denominations')
