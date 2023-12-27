import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

rows, cols = map(int, input().split())

table = [[*map(int, input().split())] for _ in range(rows)]

dp = [[-1]*cols for _ in range(rows)]

directions = ((1,0),(0,1),(-1,0),(0,-1))

def dfs(start = (0,0)):
    x, y = start
    if x==rows-1 and y == cols-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i,j in directions:
        nx, ny = x+i, y+j
        if 0<=nx<rows and 0<=ny<cols and table[nx][ny] < table[x][y]:
            dp[x][y] += dfs((nx,ny))
    return dp[x][y]

print(dfs())
