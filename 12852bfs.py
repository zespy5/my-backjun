import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

table = [-1]*1000001

def bfs(N):
    
    que = deque()
    que.append(N)
    table[N] = N
    
    while(que):
        now = que.popleft()
        if now == 1:
            return
        
        if now%3 == 0:
            nex = now//3
            if table[nex] == -1:
                que.append(nex)
                table[nex] = now
        
        if now%2 == 0:
            nex = now//2
            if table[nex] == -1:
                que.append(nex)
                table[nex] = now
        
        nex = now -1
        if table[nex] == -1:
            que.append(nex)
            table[nex] = now

steps = []

def dfs(n):
    if n == table[n]:
        steps.append(n)
        return
    dfs(table[n])
    steps.append(n)
    return

bfs(N)
dfs(1)
print(len(steps)-1)
for i in steps:
    print(i, end=' ')

    