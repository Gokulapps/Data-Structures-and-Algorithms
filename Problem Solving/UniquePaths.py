# Dynamic Programming Algorithm to solve number of unique paths available 
def uniquePaths(rows, columns): 
    result_grid = [[0 for j in range(columns)] for i in range(rows)]
    for row in range(rows-1, -1, -1):
        for col in range(columns-1, -1 , -1):
            if row == (rows - 1) or (col == columns - 1):
                result_grid[row][col] = 1 
            else: 
                result_grid[row][col] = result_grid[row+1][col] + result_grid[row][col+1]
    return result_grid[0][0]
    
answer = uniquePaths(3, 7)
print("The Number of Unique Paths available is: ", answer)
