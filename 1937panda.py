import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)

directions = ((1,0),(0,1),(-1,0),(0,-1))
N = int(input())

forest = [[*map(int, input().split())] for _ in range(N)]

visited = [[0]*N for _ in range(N)]
ans = 1

def dfs(x,y):
    
    global ans
    
    if visited[x][y]:
        return visited[x][y]
    
    visited[x][y] = 1
    
    for i,j in directions:
        nx,ny = x+i,y+j
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        if forest[x][y] < forest[nx][ny]:
            count = 1
            count += dfs(nx,ny)
            visited[x][y] = max(visited[x][y], count)
            ans = max(ans, visited[x][y])
    return visited[x][y]


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)

print(ans)