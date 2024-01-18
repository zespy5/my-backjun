import sys
from collections import deque

INF = 999999
directions = ((1,0),(0,1),(-1,0),(0,-1))

input = sys.stdin.readline

N = int(input())

island_map = [[*map(int, input().split())] for _ in range(N)]

def find_sections():
    visited = [[0]*N for _ in range(N)]
    
    lands = []
    
    def bfs(x,y):
        if not island_map[x][y]:
            visited[x][y] = 1
            return
        
        if visited[x][y]:
            return
        
        visitedset = set()
        que = deque()
        que.append((x,y))
        visitedset.add((x,y))
        visited[x][y] = 1
        
        while(que):
            a,b = que.popleft()
            
            for i,j in directions:
                nx,ny = a+i, b+j
                if nx<0 or nx >= N or ny<0 or ny>=N:
                    continue
                if (nx,ny) in visitedset:
                    continue
                if island_map[nx][ny]:
                    que.append((nx,ny))
                    visited[nx][ny] = 1
                    visitedset.add((nx,ny))
        
        lands.append(visitedset)
        
        return
    
    for i in range(N):
        for j in range(N):
            bfs(i,j)
    
    return lands
            
lands = find_sections()

first_land = lands[0]

around = set()

for x,y in first_land:
    
    for i,j in directions:
        a,b = x+i,y+j
        
        if 0<=a<N and 0<=b<N and not island_map[a][b]:
            around.add((a,b))
            
print(around)
            