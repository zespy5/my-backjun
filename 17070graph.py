import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

house = [[*map(int, input().split())] for _ in range(N)]

end = N-1, N-1

def bfs():
    #가로는 0, 세로는 1, 대각선은 2
    #큐 내부 튜플(파이프 모형, x,y)
    end_count = 0
    
    que = deque()
    que.append((0,0,1))
    
    while(que):
        pipe, x, y = que.popleft()
        if (x,y) == end:
            end_count += 1
        
        nx, ny = x+1,y+1
        
        if pipe == 0:
            if ny < N:
                if house[x][ny] == 0:
                    que.append((0,x,ny))
                else:continue
                
                if nx < N:
                    if house[nx][y] == 0 and house[nx][ny] == 0:
                        que.append((2,nx,ny))
        elif pipe == 1:
            if nx < N:
                if house[nx][y] == 0:
                    que.append((1,nx,y))
                else: continue
                
                if ny < N:
                    if house[x][ny] == 0 and house[nx][ny] == 0:
                        que.append((2,nx,ny))
        else:
            if ny < N:
                if house[x][ny] == 0:
                    que.append((0,x,ny))
            
            if nx < N:
                if house[nx][y] == 0:
                    que.append((1,nx,y))
            
            if nx < N and ny < N:
                if house[x][ny] == 0 and house[nx][y] == 0 and house[nx][ny] == 0:
                    que.append((2,nx,ny))
    
    return end_count

print(bfs())
        
        
