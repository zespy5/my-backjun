import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
is_friend = False
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,d):
    global is_friend
    
    visited[x] = 1
    if d>4:
        is_friend = True
        return

    for nex in graph[x]:
        if not visited[nex]:
            dfs(nex,d+1)
            visited[nex] = 0
        
for i in range(N):
    visited = [0]*(N+1)
    dfs(i,1)

    if is_friend:
        break
    
if is_friend:
    print(1)
else:
    print(0)