# Algorithm 1(Brute Force) - Solving it using Backtracking Algorithm (Using Recursion)
def min_comb(amount, denomination):  
    result = []  
    minimum_coin = [float('inf')]  # Use a list to hold the minimum number of coins  
  
    def backtrack(amount, comb, curr_coins):  
        if amount == 0:  
            if curr_coins <= minimum_coin[0]:  
                if curr_coins < minimum_coin[0]:  
                    # Found a better combination with fewer coins  
                    result.clear()  
                    minimum_coin[0] = curr_coins  
                comb_sorted = sorted(comb)  
                if comb_sorted not in result:  
                    result.append(comb_sorted)  
            return  
        elif amount < 0 or curr_coins >= minimum_coin[0]:  
            return  
        else:  
            for coin in denomination:  
                comb.append(coin)  
                backtrack(amount - coin, comb, curr_coins + 1)  
                comb.pop()  
  
    # Sort denominations in descending order to try larger coins first  
    denomination.sort(reverse=True)  
    backtrack(amount, [], 0)  
    return result  
  
# Example usage:  
amount = 167  
denomination = [1, 2, 5, 10, 20, 50, 100, 500]  
combinations = min_comb(amount, denomination)  
print("Minimum number of coins:", len(combinations[0]) if combinations else 0)  
print("Combinations with minimum coins:", combinations[0]) 

# Algorithm 2(Brute Force) - Solving it using Backtracking Algorithm (Using Loop)
def min_comb(amount, denomination): 
    stack = []
    result = []
    min_coin = float('inf')
    initial_state = (
        amount, # Remaining Amount
        [], # current combinations 
        0 # Current Coins 
    )
    stack.append(initial_state)
    
    while stack: 
        rem_amount, curr_comb, curr_coin = stack.pop()
        if rem_amount == 0: 
            if curr_coin < min_coin: 
                result.clear() 
                min_coin = curr_coin 
                sorted_comb = sorted(list(curr_comb))
                if sorted_comb not in result: 
                    result.append(sorted_comb)
                continue 
        elif rem_amount < 0 or curr_coin > min_coin: 
            continue 
        else: 
            for coin in denomination: 
                if coin <= rem_amount and curr_coin + 1 < min_coin: 
                    current_state = (
                        rem_amount - coin, 
                        curr_comb + [coin], 
                        curr_coin + 1 
                        )
                    stack.append(current_state)
                        
    return result 
    
amount = 167  
denomination = [1, 2, 5, 10, 20, 50, 100, 500]  
combinations = min_comb(amount, denomination)  
print("Minimum number of coins:", len(combinations[0]) if combinations else 0)  
print("Combinations with minimum coins:", combinations[0])   

# Algorithm 3(Efficient Solution) - Solving it using Dynamic Programming 
def coinChange(amount, denomination):
    dp = [float('inf')] * (amount+1) # dp[i] will hold the minimum coins for amount i  
    coin_used = [-1] * (amount+1) # coin_used[i] will hold the coin that was last used to get to amount i
    dp[0] = 0
    for curr_amt in range(1, amount+1):
        for coin in denomination: 
            if curr_amt - coin >= 0 and dp[curr_amt - coin] + 1 < dp[curr_amt]:
                dp[curr_amt] = dp[curr_amt - coin] + 1
                coin_used[curr_amt] = coin 

    # Check if amount is not reachable  
    if dp[amount] > amount:  
        return -1, []  
  
    # Backtrack to find the coins used  
    current_amount = amount  
    combination = []  
    while current_amount > 0:  
        coin = coin_used[current_amount]  
        combination.append(coin)  
        current_amount -= coin  
  
    return dp[amount], combination  

# Example Usage: 
amount = 167  
denomination = [1, 2, 5, 10, 20, 50, 100, 500]   
min_coins, combination = coinChange(amount, denomination)  
print(f"Minimum number of coins required: {min_coins}")  
print(f"Combination of coins used: {combination}")   
