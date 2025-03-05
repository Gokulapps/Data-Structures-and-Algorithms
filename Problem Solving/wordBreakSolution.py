def wordBreak(string, wordDict):
    string_length = len(string)
    dp = [False] * (string_length + 1)
    dp[string_length] = True 
    for i in range(string_length, -1, -1):
        for word in wordDict: 
            word_length = len(word)
            if word_length + i <= string_length and string[i: i+word_length] == word: 
                dp[i] = dp[i+word_length]
            if dp[i]: 
                break 
    return dp[0] 

string = "Leetcode"
wordDict = ["Leet", "code"]
result = wordBreak(string, wordDict)
if result: 
    print(f"The String {string} can be divided into multiple words")
else: 
    print(f"The String {string} cannot be divided further")
