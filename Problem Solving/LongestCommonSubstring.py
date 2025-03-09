# Dynamic Programming Algorithm to find LCS of two strings
def lcs(text1, text2):
    dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
    res_text = ''
    for i in range(len(text1)-1, -1, -1): 
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]: 
                dp[i][j] = 1 + dp[i+1][j+1]
                res_text = text1[i] + res_text
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    
    return dp[0][0], res_text

text1 = "abcdefgh"
text2 = "adg"
result, seq = lcs(text1, text2)
print('The Length of the Longest Common String Length is:', result, 'and the LCS is:', seq)
