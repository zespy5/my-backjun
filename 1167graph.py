import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N):
    a = [*map(int, input().split())]
    b = a[1:-1]
    from_node = a[0]
    for i in range(len(b)//2):
        graph[from_node].append((b[i*2],b[2*i+1]))

        
visited = [0]*(N+1)
mnode = 0
mvalue = 0

def dfs(node, value):
    global mnode, mvalue
    
    if visited[node] == 1:
        return
    visited[node] = 1
    
    if value > mvalue:
            mvalue = value
            mnode = node
            
    for next_node,v in graph[node]:
        next_value = value + v
        
        dfs(next_node, next_value)
    
    return

dfs(1,0)

visited = [0]*(N+1)
dfs(mnode,0)
print(mvalue)
    