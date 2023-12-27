import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N,L,R = map(int, input().split())

populations = [[*map(int, input().split())] for _ in range(N)]

def make_sections():
    
    visited = [[0]*N for _ in range(N)]
    directions = ((1,0),(0,1),(-1,0),(0,-1))
    
    def dfs(start, k):
        x,y = start
        
        if visited[x][y]:
            return
        
        visited[x][y] = k
        
        for i,j in directions:
            nx, ny = x+i, y+j
            
            if nx < 0 or nx >= N or ny < 0 or ny>= N:
                continue
            
            diff = abs(populations[x][y]- populations[nx][ny])
            
            if L <= diff <= R:
                dfs((nx,ny),k)
        
        return
    
    k = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                k += 1
                dfs((i,j),k)
                
                
    return visited, k
    
answer = 0

while(1):
    visited, k = make_sections()
    
    if k == N**2:
        break
    
    pop = [0]*(k+1)
    count = [0]*(k+1)
    
    for i in range(N):
        for j in range(N):
            sec_num = visited[i][j]
            count[sec_num] += 1
            pop[sec_num] += populations[i][j]
    
    for i in range(1,k+1):
        pop[i] = pop[i]//count[i]
        
    for i in range(N):
        for j in range(N):
            sec_num = visited[i][j]
            populations[i][j] = pop[sec_num]
            
    answer += 1
        

print(answer) 