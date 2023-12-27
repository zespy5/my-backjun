#LCA#

import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())

parents = [i for i in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    f,t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)



visited = [False] * (N+1)

ranks = [0]*(N+1)
    
def dfs(x, depth):
    visited[x] = True
    ranks[x] = depth 
    
    for i in graph[x]:
        if visited[i]:
            continue
        parents[i] = x
        dfs(i,depth+1)
        
dfs(1,0)
    
def LCA(x,y):
    xdiff = 0
    ydiff = 0
    if ranks[x] > ranks[y]:
        xdiff = ranks[x] - ranks[y]
    elif ranks[y] > ranks[x]:
        ydiff = ranks[y] - ranks[x]
        
    for _ in range(xdiff):
        x = parents[x]
    
    for _ in range(ydiff):
        y = parents[y]
        
    while(x!=y):
        x = parents[x]
        y = parents[y]
    
    return x

M = int(input())

for _ in range(M):
    a,b = map(int, input().split())
    print(LCA(a,b))
