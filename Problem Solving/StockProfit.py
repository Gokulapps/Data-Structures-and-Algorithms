def maxProfit(prices):
    # State: Buying or Selling? 
    # If buy -> i+1
    # If sell -> i+2
    dp = {}
    def dfs(i, buying): 
        if i >= len(prices): 
            return 0 
        if (i, buying) in dp: 
            return dp[(i, buying)]
        if buying: 
            buying = dfs(i+1, not buying) - prices[i]
            cooldown = dfs(i+1, buying)
            dp[(i, buying)] = max(buying, cooldown)
        else:
            selling = dfs(i+2, not buying) + prices[i]
            cooldown = dfs(i+1, buying)
            dp[(i, buying)] = max(selling, cooldown)
        
        return dp[(i, buying)]
    return dfs(0, True)
    

prices = [1, 2, 3, 0, 2]  
result = maxProfit(prices)
print('The Maximum Profit that can be made in the given Stock Prices is:', result)
