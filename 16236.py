import sys
from collections import deque
from queue import PriorityQueue

input = sys.stdin.readline

INF = 99999
baby_size = 2
start = 0, 0

N = int(input())

table = [[*map(int, input().split())] for _ in range(N)]

destination = []

for i in range(N):
    for j in range(N):
        if table[i][j] == 9:
            start = i,j
            table[i][j] = 0


def dijkstra(start, size):
    destination = []
    for i in range(N):
        for j in range(N):
            if 0 < table[i][j] < size:
                destination.append((i,j))
    
    if len(destination)== 0:
        return -1,-1,-1

    grid = [[INF]*N for _ in range(N)]
    direction = ((1,0),(0,1),(-1,0),(0,-1))
    
    
    pq = PriorityQueue()
    pq.put((0,start))
    a,b = start
    grid[a][b] = 0
    
    while(not pq.empty()):
        step, posi = pq.get()
        sx, sy = posi
        
        for i, j in direction:
            nx, ny = sx+i, sy+j
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if table[nx][ny] > size:
                continue
            
            n_step = step+1
            if grid[nx][ny] > n_step:
                grid[nx][ny] = n_step
                pq.put((n_step,(nx,ny)))
                
    minimum = INF
    minimums = []
    for i,j in destination:
        if grid[i][j] == INF:
            continue
        if grid[i][j] < minimum:
            minimum = grid[i][j]
            minimums.clear()
            minimums.append((i,j))
        elif grid[i][j] == minimum:
            minimums.append((i,j))
    
    if len(minimums) == 0:
        return -1,-1,-1
    elif len(minimums) == 1:
        x,y = minimums[0]
        table[x][y] = 0
        return grid[x][y], x,y
    else:
        minimums.sort()
        x,y = minimums[0]
        table[x][y] = 0
        return grid[x][y], x,y
    

def hunting(start, size):
    move_step = 0
    x,y = start
    while(1):
        for _ in range(size):
            step, x,y = dijkstra((x,y),size)
            if step == -1:
                return move_step
            
            move_step += step
        size += 1
        
print(hunting(start, baby_size))