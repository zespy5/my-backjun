import sys
from collections import deque

input = sys.stdin.readline

table = [-1]*(10**5 + 1)
N,M = map(int, input().split())


def bfs(start, end):
    
    que = deque()
    que.append(start)
    table[start] = 0
    
    while(que):
        now = que.popleft()
        
        for i in (-1,1,2):
            step = table[now]
            if i == 2:
                nex = now*2
            else:
                nex = now+i
                step += 1
     
            if nex > 10**5 or nex < 0:
                continue
            
            if table[nex] == -1 or table[nex] > step:
                table[nex] = step
                que.append(nex)
            

if N > M:
    print(N-M)          
else:
    bfs(N,M)
    print(table[M])