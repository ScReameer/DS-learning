import numpy as np


def min_max_dist(*vectors):
    
    min_dist = None
    max_dist = None
    
    # Check each vector with each
    for vector1 in vectors:
        
        for vector2 in vectors:

            check_dist = np.linalg.norm(vector1 - vector2)
                
            if min_dist is None and max_dist is None:
                
                # Initial values    
                min_dist = check_dist
                max_dist = check_dist
                    
            else:
                    
                if min_dist == 0: 
                    min_dist = check_dist
                # Minimum shouldn't be 0 if vectors don't equals
                elif min_dist != 0 and check_dist < min_dist and check_dist > 0:
                    min_dist = check_dist
                elif check_dist > max_dist:
                    max_dist = check_dist
                else:
                    continue
                    
    return (min_dist, max_dist)
                    
    
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
print(min_max_dist(vec1, vec2, vec3))