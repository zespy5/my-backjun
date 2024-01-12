import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())

parents = [-1]*100001

def bfs(n,k):
    
    que = deque()
    que.append(n)
    parents[n] = n
    
    while(que):
        now = que.popleft()
        
        if now == k:
            return
        
        for x in [now-1, now +1, now*2]:
            if x < 0 or x >10**5:
                continue
            if parents[x] != -1:
                continue
            parents[x] = now
            que.append(x)

bfs(N,K)
route = []

    
def find_route(k):
    if k == parents[k]:
        route.append(k)
        return
    find_route(parents[k])
    route.append(k)
    return

find_route(K)

print(len(route)-1)
for i in route:
    print(i, end=' ')
    