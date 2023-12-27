import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())

x,y = map(int, input().split())

m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def find_chon(x,y):
    visited = set()
    que = deque()
    visited.add(x)
    que.append((x,0))
    
    while(que):
        now, v = que.popleft()
        
        for i in graph[now]:
            if i in visited:
                continue
            nv = v+1
            
            if i == y:
                return nv
            que.append((i,nv))
            visited.add(i)
            
    return -1
            
print(find_chon(x,y))