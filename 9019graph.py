import sys
from collections import deque

input = sys.stdin.readline

def bfs(s,e):
    
    que = deque()
    que.append((s,''))
    visited = [0]*10000
    while(que):
        s, line = que.popleft()
        
        if s == e:
            return line

        nd = (2*s)%10000
        if not visited[nd]:
            que.append((nd,line+'D'))
            visited[nd] = 1
        
        ns = (s-1)%10000
        if not visited[ns]:
            que.append((ns,line+'S'))
            visited[ns] = 1
        
        nl = (10*s+(s//1000))%10000
        if not visited[nl]:
            que.append((nl,line+'L'))
            visited[nl] = 1
            
        nr = (s//10+(s%10)*1000)%10000
        if not visited[nr]:
            que.append((nr,line+'R'))
            visited[nr] = 1
        
N = int(input())

for _ in range(N):
    s,e = map(int, input().split())
    print(bfs(s,e))