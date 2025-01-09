def pump_operations_lte(capacity, inflows):
    '''Inputs the tank capacity as an integer and inflows of waste water as 
    a time series list. Find and count pump operations to keep the volume 
    within capacity. Returns the pump operations each hour as a list.'''  
    pump_history = []
    current_volume = 0
    
    # First, we'll add each inflow into the tank until it is over capacity
    for inflow in inflows:
        pump_count = 0
        current_volume += inflow
        
        # We will operate the pump until the current volume is within capacity 
        # and we will count each operation
        while current_volume >= capacity:
            pump_count += 1
            current_volume -= capacity
        
        # We will record the number of times operated each hour into a list
        pump_history.append(pump_count)
        
    return pump_history
        
    