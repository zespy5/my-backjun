import sys
from collections import deque

input = sys.stdin.readline

directions = ((1,0),(0,1),(-1,0),(0,-1))
horse_directions = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))

K = int(input())
cols, rows = map(int, input().split())

grid = [[*map(int, input().split())] for _ in range(rows)]

def bfs():
    visited = [[[-1]*cols for _ in range(rows)] for _ in range(K+1)]
    
    que = deque()
    que.append((0,0,0))
    visited[0][0][0] = 0
    
    while(que):
        c,x,y = que.popleft()
        
        if x==rows-1 and y==cols-1:
            return visited[c][x][y]
        
        if c < K:
            for i,j in horse_directions:
                nx,ny = x+i, y+j
                if nx <0 or nx >= rows or ny < 0 or ny >= cols:
                    continue
                if visited[c+1][nx][ny]>-1 or grid[nx][ny]==1:
                    continue
                visited[c+1][nx][ny]= visited[c][x][y]+1
                que.append((c+1,nx,ny))
        
        for i,j in directions:
            nx,ny = x+i, y+j
            if nx <0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if visited[c][nx][ny]>-1 or grid[nx][ny]==1:
                continue
            visited[c][nx][ny]= visited[c][x][y]+1
            que.append((c,nx,ny))
            
    return -1

print(bfs())