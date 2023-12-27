import sys

input = sys.stdin.readline

rows, cols = map(int, input().split())

grid = [list(input().rstrip()) for _ in range(rows)]

directions = ((-1,0),(1,0),(0,-1),(0,1))

max_len = ''

def dfs(x,y,trace):
    global max_len
    for i,j in directions:
        nx, ny = x+i, y+j
        if nx<0 or nx>=rows or ny<0 or ny>=cols:
            continue
        if grid[x][y] == grid[nx][ny]:
            continue
        if grid[nx][ny] in trace:
            continue
        n_t = trace+grid[nx][ny]
        if len(n_t) > len(max_len):
            max_len = n_t
        dfs(nx, ny, n_t)
        
dfs(0,0,grid[0][0])

if len(max_len) == 0:
    print(1)
else:
    print(len(max_len))
    