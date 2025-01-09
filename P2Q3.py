def search(negation_edges, visited, start, color):
    '''Takes a graph (dictionary) of negation edges, visited nodes, a node to 
    start reasoning from and its color. Group the nodes(gnome IDs). Returns the 
    white and black IDs from the graph in a tuple'''
    stack = []
    stack.append(start)
    stack_dict = {}
    
    # We will go through each connected node using Depth First Search (DFS)
    while stack:
        start = stack.pop()
        
        # First, we'll add the new ID and its inverted color into visited nodes 
        if start not in visited:       
            
            #  We'll set the color of the new ID to the deduced color 
            if start in stack_dict:
                color = stack_dict.get(start) 
                
            visited[start] = not color  
            
            # Next, we'll update all the linked IDs and their colors in stack 
            for linked in negation_edges[start]:
                stack.append(linked)
                stack_dict[linked] = not color
                
        else:
            try:
                # Here, we will check the visited IDs for contradictions
                assert(not visited[start] == stack_dict[start])
            except AssertionError:
                return None  
           
            # If the starting node is already visited, we ignore its neighbours
            except KeyError:
                pass                      
            
    # Finally, we'll output the ID list of white and black hat gnomes
    return (sorted([ids for ids, colour in visited.items() if not colour]),
           sorted([ids for ids, colour in visited.items() if colour]))           