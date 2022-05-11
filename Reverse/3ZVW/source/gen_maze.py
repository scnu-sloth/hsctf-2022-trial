import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
 
num_rows = 16
num_cols = 16
# maze_data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 3, 8, 1, 3, 10, 11, 10, 11, 11, 11, 9, 3, 10, 11, 10, 9, 0], [0, 7, 10, 15, 14, 8, 6, 8, 5, 4, 4, 6, 15, 8, 4, 2, 12, 0], [0, 5, 3, 14, 9, 2, 10, 10, 15, 10, 11, 8, 7, 11, 11, 10, 8, 0], [0, 4, 7, 9, 7, 11, 11, 8, 4, 3, 15, 8, 5, 5, 7, 11, 8, 0], [0, 3, 13, 4, 5, 5, 7, 8, 2, 13, 6, 9, 5, 4, 5, 4, 1, 0], [0, 5, 4, 1, 4, 5, 6, 8, 2, 15, 9, 4, 4, 2, 15, 8, 5, 0], [0, 5, 1, 7, 8, 6, 10, 9, 1, 4, 7, 11, 10, 8, 6, 10, 13, 0], [0, 7, 15, 13, 2, 9, 1, 6, 13, 2, 13, 6, 9, 2, 11, 11, 12, 0], [0, 5, 5, 7, 11, 14, 12, 1, 7, 9, 5, 1, 6, 9, 4, 4, 1, 0], [0, 5, 4, 4, 5, 1, 3, 12, 4, 4, 4, 7, 8, 6, 11, 11, 13, 0], [0, 6, 11, 8, 7, 15, 15, 10, 11, 10, 11, 14, 11, 9, 5, 5, 5, 0], [0, 2, 15, 8, 5, 4, 7, 9, 5, 2, 14, 9, 5, 4, 4, 5, 5, 0], [0, 3, 15, 9, 7, 8, 4, 4, 6, 9, 2, 12, 6, 9, 3, 13, 5, 0], [0, 5, 5, 4, 6, 11, 10, 8, 1, 7, 10, 8, 1, 4, 4, 5, 5, 0], [0, 4, 7, 11, 8, 7, 10, 11, 13, 6, 11, 10, 15, 9, 1, 4, 5, 0], [0, 2, 12, 4, 2, 12, 2, 12, 4, 2, 14, 8, 4, 6, 14, 8, 4, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
maze_data = [[3, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9], [5, 3, 8, 1, 3, 10, 11, 10, 11, 11, 11, 9, 3, 10, 11, 10, 9, 5], [5, 7, 10, 15, 14, 8, 6, 8, 5, 4, 4, 6, 15, 8, 4, 2, 12, 5], [5, 5, 3, 14, 9, 2, 10, 10, 15, 10, 11, 8, 7, 11, 11, 10, 8, 5], [5, 4, 7, 9, 7, 11, 11, 8, 4, 3, 15, 8, 5, 5, 7, 11, 8, 5], [5, 3, 13, 4, 5, 5, 7, 8, 2, 13, 6, 9, 5, 4, 5, 4, 1, 5], [5, 5, 4, 1, 4, 5, 6, 8, 2, 15, 9, 4, 4, 2, 15, 8, 5, 5], [5, 5, 1, 7, 8, 6, 10, 9, 1, 4, 7, 11, 10, 8, 6, 10, 13, 5], [5, 7, 15, 13, 2, 9, 1, 6, 13, 2, 13, 6, 9, 2, 11, 11, 12, 5], [5, 5, 5, 7, 11, 14, 12, 1, 7, 9, 5, 1, 6, 9, 4, 4, 1, 5], [5, 5, 4, 4, 5, 1, 3, 12, 4, 4, 4, 7, 8, 6, 11, 11, 13, 5], [5, 6, 11, 8, 7, 15, 15, 10, 11, 10, 11, 14, 11, 9, 5, 5, 5, 5], [5, 2, 15, 8, 5, 4, 7, 9, 5, 2, 14, 9, 5, 4, 4, 5, 5, 5], [5, 3, 15, 9, 7, 8, 4, 4, 6, 9, 2, 12, 6, 9, 3, 13, 5, 5], [5, 5, 5, 4, 6, 11, 10, 8, 1, 7, 10, 8, 1, 4, 4, 5, 5, 5], [5, 4, 7, 11, 8, 7, 10, 11, 13, 6, 11, 10, 15, 9, 1, 4, 5, 5], [5, 2, 12, 4, 2, 12, 2, 12, 4, 2, 14, 8, 4, 6, 14, 8, 4, 5], [6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 12]]
# The array M is going to hold the array information for each cell.
# The first four coordinates tell if walls exist on those sides 
# and the fifth indicates if the cell has been visited in the search.
# M(LEFT, UP, RIGHT, DOWN, CHECK_IF_VISITED)
M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)
 
# The array image is going to be the output image to display
image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)
 
# # Set starting row and column
# r = 0
# c = 0
# history = [(r,c)] # The history is the stack of visited locations

# # Trace a path though the cells of the maze and open walls along the path.
# # We do this with a while loop, repeating the loop until there is no history, 
# # which would mean we backtracked to the initial start.
# while history: 
#     #random choose a candidata cell from the cell set histroy
#     r,c = random.choice(history)
#     M[r,c,4] = 1 # designate this location as visited
#     history.remove((r,c))
#     check = []
#     # If the randomly chosen cell has multiple edges 
#     # that connect it to the existing maze, 
#     if c > 0:
#         if M[r,c-1,4] == 1:
#             check.append('L')
#         elif M[r,c-1,4] == 0:
#             history.append((r,c-1))
#             M[r,c-1,4] = 2
#     if r > 0:
#         if M[r-1,c,4] == 1: 
#             check.append('U') 
#         elif M[r-1,c,4] == 0:
#             history.append((r-1,c))
#             M[r-1,c,4] = 2
#     if c < num_cols-1:
#         if M[r,c+1,4] == 1: 
#             check.append('R')
#         elif M[r,c+1,4] == 0:
#             history.append((r,c+1))
#             M[r,c+1,4] = 2 
#     if r < num_rows-1:
#         if M[r+1,c,4] == 1: 
#             check.append('D') 
#         elif  M[r+1,c,4] == 0:
#             history.append((r+1,c))
#             M[r+1,c,4] = 2
 
#     # select one of these edges at random.
#     if len(check):
#         move_direction = random.choice(check)
#         if move_direction == 'L':
#             M[r,c,0] = 1
#             c = c-1
#             M[r,c,2] = 1
#         if move_direction == 'U':
#             M[r,c,1] = 1
#             r = r-1
#             M[r,c,3] = 1
#         if move_direction == 'R':
#             M[r,c,2] = 1
#             c = c+1
#             M[r,c,0] = 1
#         if move_direction == 'D':
#             M[r,c,3] = 1
#             r = r+1
#             M[r,c,1] = 1

# maze_data = [[0 for _ in range(num_cols+2)]]
# for i in range(num_rows):
#     tmpl = [0]
#     for j in range(num_cols):
#         data = ""
#         for k in range(4):
#             data += str(M[i,j,k])
#         tmpl.append(int(data, 2))
#     tmpl.append(0)
#     maze_data.append(tmpl)
# maze_data.append([0 for _ in range(num_cols+2)])
# print(maze_data)

# for i in range(num_rows+2):
#     for j in range(num_cols+2):
#         if i == 0 and j == 0:
#             maze_data[i][j] |= 0b0011
#         elif i == 0 and j == num_cols+1:
#             maze_data[i][j] |= 0b1001
#         elif i == num_rows+1 and j == 0:
#             maze_data[i][j] |= 0b0110
#         elif i == num_rows+1 and j == num_cols+1:
#             maze_data[i][j] |= 0b1100
#         elif i == 0:
#             maze_data[i][j] |= 0b1010
#         elif j == 0:
#             maze_data[i][j] |= 0b0101
#         elif i == num_rows+1:
#             maze_data[i][j] |= 0b1010
#         elif j == num_cols+1:
#             maze_data[i][j] |= 0b0101
# maze_data[13][16] |= 0b10010
# print(maze_data)

def getVal(arr, t):
    return arr[t[0]][t[1]]

def walkMaze(start, end):
    dirs = [(0,-1), (-1,0), (0,1), (1,0)]
    # FLAG_CHAR = ['a', 'w', 'd', 's']
    FLAG_CHAR = ['h', 'k', 'l', 'j']
    path = [start]
    step = [["" for _ in range(num_cols+2)] for _ in range(num_rows+2)]
    flag = ""
    while len(path) != 0:
        prev = path[0]
        del path[0]
        for i in range(4):
            cur = (prev[0]+dirs[i][0], prev[1]+dirs[i][1])
            if getVal(maze_data, prev)&(1<<(3-i)) != 0 and getVal(step, cur) == "":
                step[cur[0]][cur[1]] = getVal(step, prev) + FLAG_CHAR[i]
                path.append(cur)
    return getVal(step, end)

print("(13, 16): ", walkMaze((1, 1), (13, 16)))

for i in range(0, num_rows):
    for j in range(0, num_cols):
        for k in range(4):
            M[i,j,k] = ((maze_data[i+1][j+1])&(1<<(3-k)))>>(3-k)
        if maze_data[i+1][j+1] > 15:
            M[i,j,4] = 1

# Open the walls at the start and finish
fin = (13, 16)
# M[0,0,1] = 1
# M[fin[0]-1,fin[1]-1,2] = 1
# Generate the image for display
for row in range(0,num_rows):
    for col in range(0,num_cols):
        cell_data = M[row,col]
        if cell_data[4] == 0:
            for i in range(10*row+2,10*row+8):
                image[i,range(10*col+2,10*col+8)] = 255
        else:
            for i in range(10*row+2,10*row+8):
                image[i,range(10*col+2,10*col+8)] = 128
        if cell_data[0] == 1: 
            image[range(10*row+2,10*row+8),10*col] = 255
            image[range(10*row+2,10*row+8),10*col+1] = 255
        if cell_data[1] == 1: 
            image[10*row,range(10*col+2,10*col+8)] = 255
            image[10*row+1,range(10*col+2,10*col+8)] = 255
        if cell_data[2] == 1: 
            image[range(10*row+2,10*row+8),10*col+9] = 255
            image[range(10*row+2,10*row+8),10*col+8] = 255
        if cell_data[3] == 1: 
            image[10*row+9,range(10*col+2,10*col+8)] = 255
            image[10*row+8,range(10*col+2,10*col+8)] = 255
        
 
# Display the image
plt.imshow(image, cmap = cm.Greys_r, interpolation='none')
plt.show()