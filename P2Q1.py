BOTH_WHITE = 2
BOTH_BLACK = 0
ID = 0
COLOR = 1

def get_colors_straightforward(evidences):
    '''Takes a list of evidences in tuples. Finds all gnomes with white and 
    black hats in same-color-pairs. Returns a tuple of two sorted lists of 
    gnome-IDs or None if there is a contradiction.'''
    # We will store the gnome IDs in sets to avoid redundant information
    white = set()     
    black = set()
    
    # We will checks each evidence for same-color-pairs
    # Then, we will group the gnome IDs by their colors
    for evidence in evidences:
        if evidence[COLOR] == BOTH_BLACK:
            for gnome_id in evidence[ID]:
                black.add(gnome_id)
                
        if evidence[COLOR] == BOTH_WHITE:
            for gnome_id in evidence[ID]:
                white.add(gnome_id)
    
    # Contradiction will occur if an ID is listed as both white and black 
    if white.intersection(black):
        return None
    
    # Outputs the grouped IDs in a tuple
    return sorted(white), sorted(black)