def rob(houses): 
    rob1 = 0 
    rob2 = 0
    for house in houses: 
        temp = max(rob1+house, rob2)
        rob1 = rob2 
        rob2 = temp 
    
    return rob2 
    
houses = [1, 4, 5, 2, 1, 6]
max_amount = max(houses[0], rob(houses[1:]), rob(houses[:-1]))
print('The Maximum Amount that can be robbed is: ', max_amount)
