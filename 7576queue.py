import sys
from collections import deque


inp = sys.stdin.readline
directions = ((1,0),(0,1),(-1,0),(0,-1))

cols, rows = map(int, inp().split())
input_grid = [list(map(int, inp().split())) for _ in range(rows)]
    
fifo = deque()

for i in range(rows):
    for j in range(cols):
        if input_grid[i][j] == 1:
            fifo.append((i,j,1))

cnt = 0
       
while(fifo):
    r,c,cnt = fifo.popleft()

    for x,y in directions:
        nr, nc = r+x, c+y
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
            continue
        if input_grid[nr][nc] != 0:
            continue
        
        ncnt = cnt+1
        input_grid[nr][nc] = ncnt
        fifo.append((nr,nc,ncnt))
        
for i in input_grid:
    if 0 in i:
        print(-1)
        sys.exit()

print(cnt-1)
