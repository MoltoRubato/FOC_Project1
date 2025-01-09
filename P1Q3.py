def predict_lte(current, past):
    '''Accepts current time series and a list of past time series as input. 
    Finds a past case that is most similar to current case. Outputs the next 
    predicted water level using the next value of that past case.'''
    mindiff = float('inf')
    result = 0
    
    for past_case in past:
        # First, we check how similar each past case is to the current case
        diff = sum(abs(current[indx] - past_case[indx]) 
                   for indx in range(len(current)))
        
        # When we find a past case more similar than previously checked ones,
        # we will change our prediction of the next value using that case
        if diff < mindiff:
            mindiff = diff
            result = past_case[-1]
    
    return result
