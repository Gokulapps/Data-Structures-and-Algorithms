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
print(f"Total No of Ways to sum up to the given amount {amount} is:", totalWays)

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
print(f"Total No of Ways to sum up to the given amount {amount} is:", totalWays)

# Algorithm 3 - Dynamic Programming Solution 
