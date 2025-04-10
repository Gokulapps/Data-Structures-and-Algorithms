def distinctSubsequence(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    cache = {}
    def dfs(i, j):
        if j == str2_len: 
            return 1 
        if i == str1_len:
            return 0 
        if (i, j) in cache: 
            return cache[(i, j)]
        if str1[i] == str2[j]: 
            cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
        else: 
            cache[(i, j)] = dfs(i+1, j)
        return cache[(i, j)]
    return dfs(0, 0)
        
str1 = "Rasxsbsaxbxit"
str2 = "Rabbit"
print(f'The Number of Distinct Subsequence of {str2} in {str1} is: {distinctSubsequence(str1, str2)}')
