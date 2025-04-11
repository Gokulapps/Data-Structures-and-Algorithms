def operationsRequired(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    cache = {}
    def dfs(i, j):
        if i == str1_len and j == str2_len: 
            return 0 
        if j == str2_len: 
            return str1_len - i 
        if i == str1_len:
            return str2_len - j  
        if (i, j) in cache: 
            return cache[(i, j)]
        if str1[i] == str2[j]: 
            cache[(i, j)] = dfs(i+1, j+1)
        else: 
            cache[(i, j)] = 1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
        return cache[(i, j)]
    return dfs(0, 0)
        
str1 = "acd"
str2 = "abd"
print(f'The Number of Operations required to convert `{str1}` to `{str2}` is:', operationsRequired(str1, str2))
