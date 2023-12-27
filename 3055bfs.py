import sys
from collections import deque

input = sys.stdin.readline

rows, cols = map(int, input().split())

forest = [[*input().rstrip()] for _ in range(rows)]
directions = ((1,0),(0,1),(-1,0),(0,-1))
start = 0,0
end = 0,0
magic_ball = []

for i in range(rows):
    for j in range(cols):
        if forest[i][j] == 'S':
            start = i,j
        elif forest[i][j] == 'D':
            end = i,j
        elif forest[i][j] == '*':
            magic_ball.append((i,j))
            
            
def bfs(S,E):
    global rows, cols
    x,y = S
    que = deque()

    que.append((x,y,0))
    for x,y in magic_ball:
        que.append((x,y,0))
        
    while(que):
        x,y,d = que.popleft()
        
        if (x,y) == E:
            return d
        for i,j in directions:
            nx, ny = x+i, y+j
            if 0<=nx< rows and 0 <= ny < cols:
                if forest[x][y] == 'S' and (forest[nx][ny] == '.' or forest[nx][ny]== 'D'):
                    forest[nx][ny] = 'S'
                    que.append((nx,ny,d+1))
                elif forest[x][y] == '*' and (forest[nx][ny]== '.' or forest[nx][ny]== 'S'):
                    forest[nx][ny] = '*'
                    que.append((nx,ny,d+1))
                
    
    return 'KAKTUS'

print(bfs(start, end))

for i in forest:
    print(i)