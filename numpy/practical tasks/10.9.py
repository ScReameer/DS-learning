import numpy as np


def any_normal(*vectors):
    
    perpendicular = False
    
    for index_1, vector in enumerate(vectors):
        
        for index_2 in range(index_1 + 1, len(vectors)):
            
            if np.dot(vector, vectors[index_2]) == 0:
                perpendicular = True
    
    return perpendicular

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))
# True