# Algorithm 1 - Top down Dynamic Programming Approach
def decode(string):
    if not string or string[0] == '0':
        return 0 
    result = dict()
    length = len(string)
    def dfs(i, string, length): 
        ways = 0
        if i >= length: 
            return 1
        elif string[i] == '0':
            return 0
        elif i == (length - 1): 
            return 1 
        elif result.get(i, False):
            return result[i]
        elif string[i] == '1' or (string[i] == '2' and string[i+1] in '123456'):
            ways = dfs(i+1, string, length) + dfs(i+2, string, length)
            result[i] = ways
            return ways
        else: 
            ways = dfs(i+1, string, length)
            result[i] = ways
            return ways
            
    return dfs(0, string, length)
    
string = '12134'
print(decode(string))

# Algorithm 2 - Bottom up Dynamic Programming Approach using dp array
def decodeWays(string):  
    if not string or string[0] == '0':  
        return 0  
      
    length = len(string)  
    dp = [0] * (length + 1)  
    dp[0] = 1  
    dp[1] = 1  
      
    for i in range(2, length + 1):  
        if string[i-1] != '0':  
            dp[i] += dp[i-1]  
        if string[i-2] == '1' or (string[i-2] == '2' and string[i-1] in '0123456'):  
            dp[i] += dp[i-2]  
      
    return dp[length]  
  
string = '101'  
print(decodeWays(string))

# Algorithm 3 - Bottom up Dynamic Programming Approach using only two variable 
def decodeWays(string):  
    if not string or string[0] == '0':  
        return 0  
      
    length = len(string)    
    prev_val = 1
    curr_val = 1
      
    for i in range(2, length + 1):  
        next_val = 0
        if string[i-1] != '0':  
            next_val += curr_val
        if string[i-2] == '1' or (string[i-2] == '2' and string[i-1] in '0123456'):  
            next_val += prev_val
        prev_val, curr_val = curr_val, next_val
      
    return curr_val  
  
string = '12345167'  
print(decodeWays(string))  
