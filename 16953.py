import sys
from collections import deque

input = sys.stdin.readline

x,y = map(int, input().split())


def bfs(x,y):
    
    que = deque()
    que.append((x,1))
    
    while(que):
        now, dep = que.popleft()
        
        nd = dep+1
        
        for k in now*2, now*10+1:
            if k == y:
                return nd
            elif k > y:
                continue
            
            que.append((k,nd)) 
            
    return -1

print(bfs(x,y))