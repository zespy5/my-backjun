import sys
from queue import PriorityQueue
from collections import deque

INF = 9999999
input = sys.stdin.readline

directions = ((1,0),(0,1),(-1,0),(0,-1))

rows, cols = map(int, input().split())

grid = [list(map(int, list(input().rstrip()))) for _ in range(rows)]
walls = []
roads = []


for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            grid[i][j] = -1
            walls.append((i,j))
        else:
            roads.append((i,j))
  
    
def find_sections():
    
    outter_visited = set()
    sections = []
    
    def bfs(start):
        global rows, cols
        if start in outter_visited:
            return
        
        visited = set()
        que = deque()
        
        outter_visited.add(start)
        visited.add(start)
        que.append(start)
        
        while(que):
            x,y = que.popleft()
            
            for i, j in directions:
                nx, ny = x+i, y+j
                
                if nx < 0 or nx >= rows or ny < 0 or ny >=cols:
                    continue
                next_p = (nx, ny)
                
                if next_p in visited:
                    continue
                
                if grid[nx][ny]==0:
                    que.append(next_p)
                    visited.add(next_p)
                    outter_visited.add(next_p)
        
        sections.append(visited)
    
    for s in roads:
        bfs(s)
    
    return len(sections)



if find_sections() >4:
    print(-1,'s')
    sys.exit()
    
if len(roads) < rows+cols-2:
    print(-1,'l')
    sys.exit()
    
    

def dijkstra(wall):
    global rows, cols
    
    inst_grid = [[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                inst_grid[i][j] = INF
            else:
                inst_grid[i][j] = grid[i][j]
            
    wx, wy = wall
    inst_grid[wx][wy] = INF
    
    
    inst_grid[0][0] = 1
    PQ = PriorityQueue()
    PQ.put((1,(0,0)))
    
    while(not PQ.empty()):
        step, xy = PQ.get()
        x, y = xy
        
        for i, j in directions:
            nx, ny = x+i, y+j
            if nx<0 or nx>=rows or ny<0 or ny>=cols:
                continue
            
            if inst_grid[nx][ny] > 0:
                n_step = step+1
                n_p = (nx,ny)
                if inst_grid[nx][ny] > n_step:
                    inst_grid[nx][ny] = n_step
                    PQ.put((n_step, n_p))
                    
                    
    return inst_grid[rows-1][cols-1]


ans = []
ans.append(dijkstra((0,0)))
for p in walls:
    ans.append(dijkstra(p))
    
    
if all(a == INF for a in ans):
    print(-1)
else:
    print(min(ans))
            
        
        
    
                