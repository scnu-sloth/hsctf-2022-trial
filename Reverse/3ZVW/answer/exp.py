def getVal(arr, t):
    return arr[t[0]][t[1]]

def walkMaze(maze_data, lens, start, end):
    dirs = [(0,-1), (-1,0), (0,1), (1,0)]
    FLAG_CHAR = ['h', 'k', 'l', 'j']
    path = [start]
    step = [["" for _ in range(lens)] for _ in range(lens)]
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

maze = [0x03, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x09, 0x05, 0x03, 0x08, 0x01, 0x03, 0x0A, 0x0B, 0x0A, 0x0B, 0x0B, 0x0B, 0x09, 0x03, 0x0A, 0x0B, 0x0A, 0x09, 0x05, 0x05, 0x07, 0x0A, 0x0F, 0x0E, 0x08, 0x06, 0x08, 0x05, 0x04, 0x04, 0x06, 0x0F, 0x08, 0x04, 0x02, 0x0C, 0x05, 0x05, 0x05, 0x03, 0x0E, 0x09, 0x02, 0x0A, 0x0A, 0x0F, 0x0A, 0x0B, 0x08, 0x07, 0x0B, 0x0B, 0x0A, 0x08, 0x05, 0x05, 0x04, 0x07, 0x09, 0x07, 0x0B, 0x0B, 0x08, 0x04, 0x03, 0x0F, 0x08, 0x05, 0x05, 0x07, 0x0B, 0x08, 0x05, 0x05, 0x03, 0x0D, 0x04, 0x05, 0x05, 0x07, 0x08, 0x02, 0x0D, 0x06, 0x09, 0x05, 0x04, 0x05, 0x04, 0x01, 0x05, 0x05, 0x05, 0x04, 0x01, 0x04, 0x05, 0x06, 0x08, 0x02, 0x0F, 0x09, 0x04, 0x04, 0x02, 0x0F, 0x08, 0x05, 0x05, 0x05, 0x05, 0x01, 0x07, 0x08, 0x06, 0x0A, 0x09, 0x01, 0x04, 0x07, 0x0B, 0x0A, 0x08, 0x06, 0x0A, 0x0D, 0x05, 0x05, 0x07, 0x0F, 0x0D, 0x02, 0x09, 0x01, 0x06, 0x0D, 0x02, 0x0D, 0x06, 0x09, 0x02, 0x0B, 0x0B, 0x0C, 0x05, 0x05, 0x05, 0x05, 0x07, 0x0B, 0x0E, 0x0C, 0x01, 0x07, 0x09, 0x05, 0x01, 0x06, 0x09, 0x04, 0x04, 0x01, 0x05, 0x05, 0x05, 0x04, 0x04, 0x05, 0x01, 0x03, 0x0C, 0x04, 0x04, 0x04, 0x07, 0x08, 0x06, 0x0B, 0x0B, 0x0D, 0x05, 0x05, 0x06, 0x0B, 0x08, 0x07, 0x0F, 0x0F, 0x0A, 0x0B, 0x0A, 0x0B, 0x0E, 0x0B, 0x09, 0x05, 0x05, 0x05, 0x05, 0x05, 0x02, 0x0F, 0x08, 0x05, 0x04, 0x07, 0x09, 0x05, 0x02, 0x0E, 0x09, 0x05, 0x04, 0x04, 0x05, 0x05, 0x05, 0x05, 0x03, 0x0F, 0x09, 0x07, 0x08, 0x04, 0x04, 0x06, 0x09, 0x02, 0x0C, 0x06, 0x09, 0x03, 0x0D, 0x17, 0x05, 0x05, 0x05, 0x05, 0x04, 0x06, 0x0B, 0x0A, 0x08, 0x01, 0x07, 0x0A, 0x08, 0x01, 0x04, 0x04, 0x05, 0x05, 0x05, 0x05, 0x04, 0x07, 0x0B, 0x08, 0x07, 0x0A, 0x0B, 0x0D, 0x06, 0x0B, 0x0A, 0x0F, 0x09, 0x01, 0x04, 0x05, 0x05, 0x05, 0x02, 0x0C, 0x04, 0x02, 0x0C, 0x02, 0x0C, 0x04, 0x02, 0x0E, 0x08, 0x04, 0x06, 0x0E, 0x08, 0x04, 0x05, 0x06, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0C]
a = 18
for i in range(len(maze)):
    if maze[i] & 0x10 != 0:
        break
end = (i//a, i%a)
maze = list(zip(*[iter(maze)] * a))
flag = "hsctf{" + walkMaze(maze, a, (1, 1), end) + "}"
print(flag)