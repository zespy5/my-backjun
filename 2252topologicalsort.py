import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

in_degree = [0]*N

graph=[[] for _ in range(N)]

for _ in range(M):
    f, t = map(int, input().split())
    f, t = f-1, t-1
    in_degree[t] += 1
    graph[f].append(t)
    
def find_zeros_index():
    zeros_index = [i for i in range(N) if in_degree[i]==0]
    return zeros_index

que = deque()
zeros = find_zeros_index()
for x in zeros:
    que.append(x)

while(que):
    now = que.popleft()
    print(now+1, end=' ')
    in_degree[now] = -1
    
    for n in graph[now]:
        in_degree[n] -= 1
        
        if in_degree[n] == 0:
            que.append(n)