import numpy as np


def min_max_dist(*vectors):
    
    min_dist = None
    max_dist = None
    
    # Check each vector with each but without repeats
    for index_1, vector1 in enumerate(vectors):
        
        for index_2 in range(index_1 + 1, len(vectors)):

            check_dist = np.linalg.norm(vector1 - vectors[index_2])
                
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
vec4 = np.array([9, 10, 11])
vec5 = np.array([0.3, 0.5, 0.9])

 
print(min_max_dist(vec1, vec2, vec3, vec4, vec5))