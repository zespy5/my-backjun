import sys
from collections import deque

input = sys.stdin.readline

directions = ((1,0),(0,1),(-1,0),(0,-1))
cols, rows = map(int, input().split())

miro = [[*map(int, [*input().rstrip()])] for _ in range(rows)]

dp = [[-1]*cols for _ in range(rows)]

def bfs():
    global rows, cols
    
    que = deque()
    que.append((0,0))
    dp[0][0] = 0
    
    while(que):
        x,y = que.popleft()
        
        for i,j in directions:
            nx,ny = x+i, y+j
            
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            
            if dp[nx][ny] < 0:
                if miro[nx][ny]:
                    dp[nx][ny] = dp[x][y]+1
                    que.append((nx,ny))
                else:
                    dp[nx][ny] = dp[x][y]
                    que.append((nx,ny))
            else:
                if miro[nx][ny]:
                    if dp[nx][ny] > dp[x][y]+1:
                        dp[nx][ny] = dp[x][y]+1
                        que.append((nx,ny))
                else:
                    if dp[nx][ny] > dp[x][y]:
                        dp[nx][ny] = dp[x][y]
                        que.append((nx,ny))
                        
    return dp[rows-1][cols-1]

print(bfs())
  
                    
            