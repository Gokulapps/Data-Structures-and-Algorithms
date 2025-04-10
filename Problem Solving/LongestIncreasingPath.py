def LongestIncreasingPath(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    cache = {}
    
    def dfs(row, col, prevVal):
        if row < 0 or row >= rows or col < 0 or col >= columns or matrix[row][col] <= prevVal:
            return 0, [] 
        if (row, col) in cache: 
            return cache[(row, col)]
        
        res = 1 
        max_path = [matrix[row][col]]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for new_row, new_col in directions: 
            curr_row, curr_col = row + new_row, col + new_col
            length, path = dfs(curr_row, curr_col, matrix[row][col])
            if 1 + length > res: 
                res = 1 + length
                max_path = [matrix[row][col]] + path
        
        cache[(row, col)] = res, max_path
        return res, max_path
    
    longest = 0
    max_path = []
    
    for row in range(rows): 
        for col in range(columns): 
            LIP, path = dfs(row, col, -1)
            if LIP > longest: 
                longest = LIP
                max_path = path
    
    return longest, max_path

matrix = [[2, 9, 7], 
          [1, 3, 6], 
          [5, 8, 4]]
longest_length, path = LongestIncreasingPath()
print('The Length of the Longest Increasing Path in the Given Input is: ', longest_length)
print('And the Longest Path is: ', path)
