import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    graph[a].append(b)

visited = [-1]*N
def bfs(s):
    
    que = deque()
    que.append(s)
    visited[s] = 0
    
    while(que):
        now = que.popleft()
        next_step = visited[now] +1
        
        if next_step > K:
                continue
            
        for nex in graph[now]:
            if visited[nex] > -1:
                continue
            
            visited[nex] = next_step
            que.append(nex)
            
bfs(X-1)
answer = []
for i in range(N):
    if visited[i] == K:
        answer.append(i)

if answer:
    for i in answer:
        print(i+1)
else:
    print(-1)
    
    