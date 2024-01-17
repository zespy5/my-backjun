import sys
from collections import deque

INF = 9999999
END = 100000
input = sys.stdin.readline

N,K = map(int, input().split())

visited = [0]*(END+1)

def bfs(n,k):
    
    count = 0
    
    que = deque()
    que.append(n)
    
    while(que):
        now = que.popleft()
        
        if now == k:
            count +=1
            continue
        
        for nx in [now-1, now+1, now*2]:
            if 0<=nx<=END and (visited[nx]== 0 or visited[nx]== visited[now]+1):
                visited[nx] = visited[now] +1
                que.append(nx)
                
    return count

x = bfs(N,K)
print(visited[K])
print(x)



