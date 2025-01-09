# DO NOT DELETE/EDIT THIS LINE OF CODE, AS IT IS USED TO PROVIDE ACCESS TO
# WORKING IMPLEMENTATIONS OF THE FUNCTIONS FROM Q1, Q2 and Q3. 
from hidden import get_colors_straightforward, make_color_mutex_graph, search

WHITE_IDS = 0
BLACK_IDS = 1
ID = 0
COLOR = 1
IS_BLACK = True

def resolve_colors(evidences):
    '''Takes a list of evidences. Finds and group the gnomes by hat colors. 
    Returns sorted lists of gnomes IDs with white and black hats in a tuple.'''
    # First, we'll find the colors of same-color-pairs 
    results_same = get_colors_straightforward(evidences)  
    
    # We immediately output None if we find contradictions for same-color-pairs
    if not results_same:
        return results_same
    
    # Then, we'll convert the evidence to a mutex_graph to find negation edges
    mutex_graph = make_color_mutex_graph(evidences)  
    
    # Now, we'll check if there are any different-color-pairs in evidence
    if mutex_graph:        
        visited_same = {}  # We'll use same-color results as known ID colors        
        
        # Here, we'll add the known IDs to "visited IDs" with inverted colors
        for white_id in results_same[WHITE_IDS]:
            visited_same[white_id] = not IS_BLACK
        for black_id in results_same[BLACK_IDS]:
            visited_same[black_id] = IS_BLACK
        
        # Then, we'll gather all known IDs which are possible starting points
        start_points = {}
        for key in visited_same:
            if key in mutex_graph:
                start_points[key] = not visited_same[key]
                
        # If graph doesn't contain known IDs, all colors in it is unknown
        if not start_points:
            return results_same
        
        white_final = set()
        black_final = set()
        # We'll search with all possible starting nodes to cover all systems
        for start in start_points:
            temp_visited = visited_same.copy()
            temp_visited.pop(start)
            temp_result = search(mutex_graph, temp_visited, start, 
                                 start_points[start])
            
            # We'll immediately output None if a contradiction is found
            if not temp_result:
                return None

            # Finally, we'll group all possible IDs by their colors
            for gnome in temp_result[WHITE_IDS]:
                white_final.add(gnome)
            for gnome in temp_result[BLACK_IDS]:
                black_final.add(gnome)
                
        return sorted(white_final), sorted(black_final)
    
    else:
        return results_same