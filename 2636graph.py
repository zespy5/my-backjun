import sys
from collections import deque

input = sys.stdin.readline
directions = ((1,0),(0,1),(-1,0),(0,-1))

rows, cols = map(int, input().split())

plate = [[0]*(cols+2)]

for _ in range(rows):
    i = [0]+[*map(int, input().split())]+[0]
    plate.append(i)

plate.append([0]*(cols+2))

R,C = rows+2, cols+2

def bfs():
    
    decay = set()
    
    que = deque()
    que.append((0,0))
    plate[0][0] = -1
    
    while(que):
        x,y = que.popleft()
        
        for i,j in directions:
            nx,ny = x+i,y+j
            if nx < 0 or nx >= R or ny<0 or ny >= C:
                continue
            
            if plate[nx][ny] == -1:
                continue
            
            if plate[nx][ny] == 1:
                decay.add((nx,ny))
                continue
            
            que.append((nx,ny))
            plate[nx][ny] = -1
    
    return decay


t = 0

while(1):
    is_break = True
    remained_cheeze = 0
    
    for i in range(R):
        for j in range(C):
            if plate[i][j] == 1:
                is_break = False
            elif plate[i][j] == -1:
                plate[i][j] = 0
                
    
    if is_break:
        print(t)
        print(len(decay))
        break
    
    decay = bfs()
    for x,y in decay:
        plate[x][y] = 0
        
    t+=1
    
    
    
    