import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [-1]*101
inward = set()
bs = [0]*101

for _ in range(N+M):
    a,b = map(int, input().split())
    inward.add(a)
    bs[a] = b


    
def bfs():
    
    que = deque()
    que.append(1)
    board[1] = 0
    
    while (que):
        now = que.popleft()
        
        for i in range(1,7):
            nex = now + i
            if nex > 100:
                continue
            
            
            next_step = board[now]+1
            
            if board[nex] > next_step or board[nex] == -1:

            
                board[nex] = next_step
                
                if nex in inward :
                    que.append(bs[nex])
                    if (board[bs[nex]] > next_step or board[bs[nex]] == -1):
                        board[bs[nex]] = next_step
                else:
                    que.append(nex)
                
                
bfs()
print(board[100])
            