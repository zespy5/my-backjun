import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

rows, cols = map(int, input().split())

init = [[*input().rstrip()] for _ in range(rows)]

direction = ((1,0),(0,1),(-1,0),(0,-1))
start = 0,0
end = 0,0
INF = 9999999

for i in range(rows):
    for j in range(cols):
        if init[i][j]=='S':
            start = i,j
            init[i][j] = '.'
        elif init[i][j] == 'D':
            end = i,j


def next_time(rows, cols, t_1):
    next_grid = [['.']*cols for _ in range(rows)]
    ex,ey = end
    next_grid[ex][ey] = 'D'
    
    for i in range(rows):
        for j in range(cols):
            if t_1[i][j] == 'X':
                next_grid[i][j] = 'X'
            elif t_1[i][j] == '*':
                next_grid[i][j] = '*'
                for x,y in direction:
                    ni, nj = i+x, j+y 
                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                        continue
                    if next_grid[ni][nj] != '.':
                        continue
                    next_grid[ni][nj] = '*'
                    
    return next_grid

sequence = [init]
    
minimum = INF

def dfs(D, depth):
    global minimum, rows, cols
    x,y = D
    if depth+1 >= len(sequence):
        next_grid = next_time(rows, cols, sequence[-1])
        sequence.append(next_grid)
        
    if depth >= minimum:
        return
    
    if D == end:
        if depth < minimum:
            minimum = depth
        return
    
    for i,j in direction:
        nx, ny = x+i, y+j
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            continue
        if sequence[depth+1][nx][ny] == '*':
            continue
        dfs((nx,ny), depth+1)
    
    return

dfs(start,0)

if minimum == INF:
    print('KAKTUS')
else:
    print(minimum)