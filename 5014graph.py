import sys
from collections import deque

input = sys.stdin.readline

F,S,G,U,D = map(int, input().split())

stairs = [-1]*(F+1)

def bfs(s):
    
    que = deque()
    que.append(s)
    stairs[s] = 0
    
    while(que):
        now = que.popleft()
        if now == G:
                return stairs[now]
        for n in U,-D:
            next_node = now+n
            
            if next_node < 1 or next_node > F:
                continue
            
            if stairs[next_node] != -1:
                continue

            stairs[next_node] = stairs[now]+1
            que.append(next_node)
        
    return -1

answer = bfs(S)    
if answer == -1:
    print('use the stairs')
else:
    print(answer)