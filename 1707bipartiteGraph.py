import sys
from collections import deque

input = sys.stdin.readline


N = int(input())

def bipartite_graph():
    node, edge = map(int, input().split())
    
    graph = [[] for _ in range(node+1)]
    visited = [0]*(node+1)
    for _ in range(edge):
        a,b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(n, color):
        
        if visited[n]:
            return True
        
        que = deque()
        visited[n] = color
        que.append(n)
        
        while(que):
            x = que.popleft()
            
            for i in graph[x]:
                if not visited[i]:
                    que.append(i)
                    visited[i] = -visited[x]
                else:
                    if visited[x] == visited[i]:
                        return False
        
        return True
    
    for i in range(1,node+1):
        if not bfs(i,1):
            return False
    return True

for _ in range(N):
    if bipartite_graph():
        print('YES')
    else:
        print('NO')
            
                    
                