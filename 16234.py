import sys
from collections import deque

input = sys.stdin.readline

N,L,R = map(int, input().split())

populations = [[*map(int, input().split())] for _ in range(N)]


def make_sections():
    
    outer_visited = set()
    sections = []
    directions = ((1,0),(0,1),(-1,0),(0,-1))
    
    def bfs(start):
        
        if start in outer_visited:
            return
        
        que = deque()
        inner_visited = set()
        
        que.append(start)
        inner_visited.add(start)
        
        while(que):
            x,y = que.popleft()
            
            for i,j in directions:
                nx, ny = x+i, y+j
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                
                if (nx,ny) in inner_visited:
                    continue
                
                diff = abs(populations[x][y]- populations[nx][ny])
                
                if L <= diff <= R:
                    que.append((nx,ny))
                    inner_visited.add((nx,ny))
                    outer_visited.add((nx,ny))
                    
        sections.append(inner_visited)
        
    
    for i in range(N):
        for j in range(N):
            bfs((i,j)) 
            
    return sections


answer = 0

while(1):
    sections = make_sections()
    
    if len(sections) == N**2:
        break
    
    for x in sections:
        s = 0
        for i,j in x:
            s += populations[i][j]
        size = len(x)
        
        s = s//size
        
        for i,j in x:
            populations[i][j] = s
            
    answer += 1
        

print(answer)        