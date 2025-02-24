def climbing_stairs(no_stairs): 
    n_minus_1_stair = 1
    n_minus_2_stair = 2
    if no_stairs == 1: 
        return n_minus_1_stair 
    elif no_stairs == 2: 
        return n_minus_2_stair 
    else:
        for i in range(3, no_stairs+1): 
            no_ways = n_minus_1_stair + n_minus_2_stair
            n_minus_1_stair = n_minus_2_stair
            n_minus_2_stair = no_ways 
            
    return no_ways 
    
no_stairs = 4
total_ways = climbing_stairs(no_stairs)
print(f'The Total Number of Ways to reach {no_stairs}th stair is: ', total_ways)
