def minCostClimbStairs(cost):  
    n = len(cost)  
    # dp[i] will hold the minimum cost to reach step i  
    dp = [0] * (n+1)  # Note: We need n+1 because we are considering the "top" of the staircase as a step beyond the last one.  
      
    # Fill dp array  
    for i in range(2, n + 1):  
        # To reach step i, you can either come from step i-1 or step i-2, so take the minimum of those two options.  
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])  
      
    # The answer is at dp[n], which represents the cost to reach the top (beyond the last step)  
    return dp  
  
# Example usage  
cost = [1, 2, 3, 4, 5, 6, 7]  
print(minCostClimbStairs(cost))  
