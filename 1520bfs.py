import sys
from collections import deque

input = sys.stdin.readline

rows, cols = map(int, input().split())

table = [[*map(int, input().split())] for _ in range(rows)]

directions = ((1,0),(0,1),(-1,0),(0,-1))
result = 0
def bfs():
    global result
    que = deque()
    que.append((0,0))
    
    while(que):
        x,y = que.popleft()
        
        for i,j in directions:
            nx,ny = x+i, y+j
            if 0<=nx<rows and 0<=ny<cols and table[x][y] > table[nx][ny]:
                if nx==rows-1 and ny == cols-1:
                    result+=1
                que.append((nx,ny))
                
bfs()

print(result)