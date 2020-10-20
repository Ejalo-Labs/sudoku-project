import copy, numpy, time
matrix = [[0,-3,-2],[1,-4,-2],[-3,4,1]]

def reduce(matrix,i,j):     #reduces matrix for determinant calculation
    matrix_copy = copy.deepcopy(matrix)
    matrix_copy.pop(i)
    [matrix_copy[y].pop(j) for y in range(len(matrix_copy))]
    return matrix_copy

def det(matrix):        #calucaltes determinant of a given matrix
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        return sum([(-1) ** j * matrix[0][j] * det(reduce(matrix,0,j)) for j in range(len(matrix))])

def inverse(matrix):        #calculates inverse of a matrix by cofactor method
    determinant = det(matrix)
    return "Sorry! No Inverse" if determinant == 0 else [[(-1)**(i+j)*det(reduce(matrix,j,i))/determinant for j in range(len(matrix))] for i in range(len(matrix))]

start = time.time()
print(numpy.array(inverse(matrix)))
print("\n","Runtime:  ", (time.time()-start),"\n")