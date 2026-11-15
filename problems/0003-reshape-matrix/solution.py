import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    flattened : list = []

    for i in a:
        for j in i:
            flattened.append(j)
    
    if(len(flattened)!= new_shape[0]*new_shape[1]):
        return []
    
    reshaped_matrix = np.zeros((new_shape[0],  new_shape[1]))
    k:int = 0
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            reshaped_matrix[i][j] = flattened[k]
            k+=1

    reshaped_matrix = reshaped_matrix.tolist()

    return reshaped_matrix