import numpy as np
import time

# #easy puzzle with multiple solutions
# puzzle = [[1, 0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 3, 0, 9, 0, 0, 0, 7],[0, 0, 0, 0, 2, 8, 5, 1, 0],
# [3, 0, 6, 5, 7, 0, 0, 0, 0], [0, 0, 1, 0, 0, 3, 6, 0, 0], [4, 7, 0, 6, 1, 0, 0, 0, 0],
# [0, 6, 0, 0, 3, 0, 0, 0, 0],[0, 0, 0, 8, 0, 0, 0, 5, 0],[7, 0, 0, 0, 0, 5, 1, 0, 2]]

#easy puzzle
# puzzle = [[0, 0, 0, 0, 3, 0, 0, 0, 5], [0, 4, 0, 6, 0, 9, 3, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 8],
# [7, 9, 0, 0, 0, 1, 6, 0, 3], [0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 3, 0, 9, 4, 6, 7, 0, 0],
# [3, 6, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 0, 2, 9], [0, 0, 8, 0, 0, 4, 0, 0, 0]]

# #hard puzzle
puzzle = [[0, 0, 10, 0, 0, 0, 6, 0, 0, 0, 0, 9],
[0, 4, 0, 6, 2, 0, 0, 11, 0, 0, 0, 10],
[0, 0, 0, 1, 0, 4, 0, 0, 0, 7, 0, 3],
[0, 0, 8, 0, 0, 0, 11, 1, 0, 3, 7, 12],
[1, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 5],
[0, 12, 0, 0, 5, 2, 0, 7, 4, 6, 0, 0],
[0, 0, 5, 4, 11, 0, 9, 2, 0, 0, 1, 0],
[9, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 11],
[7, 8, 12, 0, 3, 1, 0, 0, 0, 9, 0, 0],
[8, 0, 11, 0, 0, 0, 3, 0, 5, 0, 0, 0],
 [2, 0, 0, 0, 10, 0, 0, 4, 9, 0, 12, 0],
[6, 0, 0, 0, 0, 12, 0, 0, 0, 11, 0, 0]]

#really hard puzzle
puzzle = [[2,0,0,12,14,0,0,10,0,0,0,9,0,13,1,0],
[13,15,16,0,0,0,0,0,4,0,0,6,12,0,0,9],
[0,8,0,6,0,0,0,0,0,7,14,0,0,0,2,11],
[0,0,1,4,13,8,6,9,0,0,11,0,16,0,0,7],
[0,1,2,15,0,14,0,0,0,0,0,3,0,0,0,0],
[3,10,0,8,0,0,0,5,14,16,0,7,2,12,0,1],
[12,11,0,0,0,0,8,0,0,5,2,0,0,0,4,16],
[0,9,7,0,0,0,3,2,6,12,13,11,5,0,0,0],
[1,0,0,0,6,0,5,0,0,14,0,0,0,0,0,0],
[8,0,0,2,3,0,0,11,0,0,0,0,0,0,13,14],
[0,6,15,7,10,0,0,14,12,0,0,1,0,0,16,5],
[0,0,14,10,0,9,15,0,5,0,0,0,3,11,0,2],
[0,13,0,0,0,0,14,6,0,11,12,0,15,16,0,0],
[0,0,0,0,11,0,0,16,0,0,10,8,4,1,0,0],
[0,4,10,3,5,13,12,15,0,1,16,0,0,0,0,0],
[0,0,0,11,2,4,0,0,3,9,15,0,0,0,12,6]]

# # order = (3,3)
# order = (3,4)
order = (4,4)

def possible(array, row, col, order,num):        #checks if a value(num) is valid in given position(row, col) in sudoku(array) of dimension(order)
    d, r, c = order[0]*order[1], order[0], order[1]
    for i in range(0,d):        #checks possibility in rows and columns
        if array[row][i] == num or array[i][col] == num:
            return False
    row0, col0= (row//r)*r, (col//c)*c      #this block of code checks possibility in boxes
    for i in range(0, r):         #THIS CAN BE EDITED AND SHORTENED
        for j in range(0, c):
            if array[row0+i][col0+j] == num:
                return False
    return True

def solve(array, order):            #great for smaller problems
    d = order[0]*order[1]
    for row in range(d):  
        for col in range(d):
            if array[row][col] == 0:
                for num in range(1, d+1):
                    if possible(array, row,col,order,num):
                        array[row][col] = num
                        solve(array, order)
                        array[row][col] = 0
                return 
    print(np.array(array))

print(np.array((puzzle)))
print("\n", "Solving...","\n")
start = time.time()
solve(puzzle,order)
print("Solved!","\n"+"Runtime: ", (time.time()-start))