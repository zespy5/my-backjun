import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]

for _ in range(N-1):
    a,b,c = map(int, input().split())
    a,b = a-1, b-1
    graph[a].append((b,c))
    graph[b].append((a,c))

        
visited = [0]*N
max_node = 0
max_length = 0

def dfs(node, value):
    global max_node, max_length
    
    if visited[node]:
        return
    
    visited[node] = 1
    
    if value > max_length:
        max_length = value
        max_node = node
        
    for n, v in graph[node]:
        next_value = value + v
        dfs(n, next_value)
        
    return

dfs(0,0)

visited = [0]*N
dfs(max_node,0)

print(max_length)