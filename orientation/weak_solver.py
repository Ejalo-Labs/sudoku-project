import time
import numpy as np

#easy puzzle
puzzle = [[0, 0, 0, 0, 3, 0, 0, 0, 5], [0, 4, 0, 6, 0, 9, 3, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 8],
[7, 9, 0, 0, 0, 1, 6, 0, 3], [0, 0, 0, 0, 0, 0, 5, 0, 0], [0, 3, 0, 9, 4, 6, 7, 0, 0],
[3, 6, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 0, 2, 9], [0, 0, 8, 0, 0, 4, 0, 0, 0]]

# #hard puzzle
# puzzle = [[1, 0, 0, 0, 0, 0, 0, 0, 9], [0, 0, 3, 0, 9, 0, 0, 0, 7],[0, 0, 0, 0, 2, 8, 5, 1, 0],
# [3, 0, 6, 5, 7, 0, 0, 0, 0], [0, 0, 1, 0, 0, 3, 6, 0, 0], [4, 7, 0, 6, 1, 0, 0, 0, 0],
# [0, 6, 0, 0, 3, 0, 0, 0, 0],[0, 0, 0, 8, 0, 0, 0, 5, 0],[7, 0, 0, 0, 0, 5, 1, 0, 2]]

def possible_values(array,i,j):
    row_values = array[i]
    column_values = [array[k][j] for k in range(9) if array[k][j] != 0]
    box_values = [array[k][l] for k in range(i-i%3, i - i%3 + 3) for l in range(j-j%3,j-j%3+3) if array[k][l]!= 0]
    impossible_values = row_values + column_values + box_values
    return [k for k in [1,2,3,4,5,6,7,8,9] if k not in impossible_values]

def solve(array):        #solves puzzles
    for i in range(9):
        for j in range(9):
            if array[i][j] == 0 and len(possible_values(array,i,j)) == 1:
                array[i][j] = possible_values(array,i,j)[0]
    return array

def main(array):
    while True:
        if time.time() - start < 5:
            if len([array[i][j] == 0 for i in range(9) for j in range(9) if array[i][j] == 0]) > 0:
                solve(array)
            else:
                print(np.array((array,(3,3))))
                break
        else:
            print("This program is too weak. Sorry, it couldn't solve your puzzle.")
            break

start = time.time()    #stores start time to calculate total run time
print("\n"+"Solving..."+"\n")
main(puzzle)
print("\n","Runtime:  ", (time.time()-start),"\n")
