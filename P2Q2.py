from collections import defaultdict as dd

DIFF_COLOR = 1
ID = 0
COLOR = 1

def make_color_mutex_graph(evidences):
    '''Takes a list of evidences as input. Finds all links (negation_edges) 
    between gnomes. Returns a graph (dictionary) of gnomes with different hat 
    colors.'''
    # The graph will be in the form of a dictionary
    # We will first gather all linked IDs in a set to avoid redundancy
    graph = dd(set)
    diff_ids = []
    
    # First, we will pick out the ID-pairs with different hat colors
    for evidence in evidences:
        if evidence[COLOR] == DIFF_COLOR: 
            diff_ids.append(evidence[ID])
    
    # Next, we will Link those ID-pairs to each other in the graph
    for id1, id2 in diff_ids:        
        graph[id1].add(id2)
        graph[id2].add(id1)
    
    # Lastly, we will sort the IDs in an increasing order in a list
    for idnum in graph:
        graph[idnum] = sorted(graph[idnum])
    
    return dict(graph)