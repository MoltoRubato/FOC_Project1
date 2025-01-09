def volatility_lte(levels):
    '''Accepts a time series of flow levels as input. Check through all local 
    minimums and maximums of the time series. Outputs the biggest difference 
    between two successive maximum and minimum values in levels'''
    # First, we will split the time series up by the local maximum and minimums
    local_max = local_min = levels[0]
    volatility = 0    
    
    for indx in range(1, len(levels)):        
        # We will update the local max each time we see an increase 
        if levels[indx] > levels[indx - 1]:
            local_max = levels[indx]
        
        # We will also update the local min each time we see a decrease   
        elif levels[indx] < levels[indx - 1]:
            local_min = levels[indx]            
        
        # After each update, we check to see if the difference between them 
        # surpasses the biggest difference we've seen  
        if (local_max - local_min) > volatility:
            volatility = local_max - local_min
            
    return(volatility)
