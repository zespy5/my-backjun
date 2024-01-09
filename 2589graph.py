import sys
from collections import deque

input = sys.stdin.readline
directions = ((1,0),(0,1),(-1,0),(0,-1))

rows, cols = map(int, input().split())

trasure_map = [[*input().rstrip()] for _ in range(rows)]


def bfs(x,y):
    if trasure_map[x][y]=='W':
        return -1
    
    visited = [[-1]*cols for _ in range(rows)]
    
    longest_depth = 0
    
    que = deque()
    que.append((x,y))
    visited[x][y] = 0
    
    while(que):
        x,y = que.popleft()
        
        if visited[x][y] > longest_depth:
            longest_depth = visited[x][y]

            
        for i,j in directions:
            nx, ny = x+i, y+j
            if nx<0 or nx >= rows or ny <0 or ny >= cols:
                continue
            if trasure_map[nx][ny] != 'L':
                continue
            if visited[nx][ny] > -1:
                continue
            que.append((nx,ny))
            visited[nx][ny] = visited[x][y]+1
    
    return longest_depth
    
dest = 0

for i in range(rows):
    for j in range(cols):
        d = bfs(i,j)
        if d > dest:
            dest = d
            
print(dest)