import sys
import heapq as hq

INF = 999999
directions = ((1,0),(0,1),(-1,0),(0,-1))

input = sys.stdin.readline

def testcase(n):
    
    grid = [[*map(int,input().split())] for _ in range(n)]

    table = [[INF]*n for _ in range(n)]
    
    def dijkstra(k):
        
        que = []
        hq.heappush(que,(grid[0][0],0,0))
        table[0][0] = grid[0][0]
        
        while(que):
            value, x,y = hq.heappop(que)
            
            if x== k-1 and y==k-1:
                return value
            
            for i,j in directions:
                nx,ny = x+i,y+j
                
                if nx <0 or nx >= k or ny < 0 or ny >= k:
                    continue
                
                nv = value+grid[nx][ny]
                if nv < table[nx][ny]:
                    table[nx][ny] = nv
                    hq.heappush(que, (nv,nx,ny))
        
    return dijkstra(n)
                    
                
            
T = 0

while(1):
    T+=1
    N = int(input())
    
    if N == 0:
        break
    
    print(f"Problem {T}:",testcase(N))
    