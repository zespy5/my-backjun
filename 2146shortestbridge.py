import sys
from collections import deque

INF = 999999
directions = ((1,0),(0,1),(-1,0),(0,-1))

input = sys.stdin.readline

N = int(input())

island_map = [[*map(int, input().split())] for _ in range(N)]

def find_sections():
    visited = [[0]*N for _ in range(N)]
    
    def bfs(x,y,k):
        if not island_map[x][y]:
            return 0
        
        if visited[x][y]:
            return 0
        
        que = deque()
        que.append((x,y))
        visited[x][y] = k
        
        while(que):
            a,b = que.popleft()
            
            for i,j in directions:
                nx,ny = a+i, b+j
                if nx<0 or nx >= N or ny<0 or ny>=N:
                    continue
                if visited[nx][ny]:
                    continue
                if island_map[nx][ny]:
                    que.append((nx,ny))
                    visited[nx][ny] = k
        
        return 1

    areanum = 1
    for i in range(N):
        for j in range(N):
            if bfs(i,j, areanum):
                areanum+=1
    
    return visited

sections = find_sections()


minimum = INF

def find_shortest_path(x,y, m):
    if sections[x][y] == 0:
        return -1
    
    section_number = sections[x][y]
    
    visited = [[-1]*N for _ in range(N)]
    
    que = deque()
    que.append((x,y))
    visited[x][y] = 0
    
    while(que):
        x,y = que.popleft()
        
        if visited[x][y] > m:
            continue
        
        for i,j in directions:
            nx, ny = x+i, y+j
            
            if nx<0 or nx >= N or ny<0 or ny>=0:
                continue
            if section_number == sections[nx][ny]:
                continue
            if sections[nx][ny] > 0 and section_number != sections[nx][ny]:
                return visited[x][y]
            
            nd = visited[x][y]+1
            if visited[nx][ny] == -1 or visited[nx][ny] > nd:
                visited[nx][ny] = nd
                que.append((nx,ny))
    
    return -1   
            
for i in range(N):
    for j in range(N):

        m = find_shortest_path(i,j,minimum)
        print(m)

print(minimum)