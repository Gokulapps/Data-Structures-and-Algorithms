# Question: 
# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2

# Explanation:
# "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3

# Explanation:
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0

# Explanation:
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

# Constraints:
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

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
