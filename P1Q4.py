PAD = 0  # We are using padding by 0

def delay_once(delayed, undelayed):
    '''Takes 2 time series list as input. Mutate both to delay one by one hour. 
    Nothing is returned.'''
    # This pads the delayed hours using 0s
    delayed.insert(0, PAD)
    undelayed.append(PAD)

    
def find_volatility(flow1, flow2):
    '''Takes two lists of flow values as input. Finds volatility between them, 
    which is measured by the range of the combined load. Returns the 
    volatility.'''
    # This combines the two flows and finds its volatility
    combined = [flow1[i] + flow2[i] for i in range(len(flow1))]
    return max(combined) - min(combined)
    

def find_min_volatility(flows_delayed, flows_undelayed):
    '''Takes two lists of flow values as input. Delay the first flow until the 
    flows have one-hour overlap. Checks each case to find the minimum 
    volatility. Returns the minimum volatility.'''   
    # First, we set the minimum volatility to the original volatility
    min_volat = find_volatility(flows_delayed, flows_undelayed)
        
    # Next, we delay one flow and check if it gives us lower volatility  
    for _hours_delayed in range(len(flows_delayed) - 1):
        delay_once(flows_delayed, flows_undelayed) 
        volatility = find_volatility(flows_delayed, flows_undelayed)

        if volatility < min_volat:
            min_volat = volatility

    return min_volat    
    
    
def balance_lte(flows1, flows2):
    '''Takes 2 lists of flows values as input. Checks each possible scenario to 
    balance the load. Returns the volatility value of the best load balance.'''    
    # Finally, we find the lowest volatility after delaying each flow
    return min(find_min_volatility(flows1.copy(), flows2.copy()),
       find_min_volatility(flows2.copy(), flows1.copy()))
