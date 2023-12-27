import sys
from collections import deque

INF = 999999

input = sys.stdin.readline

def data_input():
    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    return N, (sx, sy), (ex, ey)

def bfs(N, start, end):
    
    directions = ((-2,-1), (-2,1), (-1,-2), (-1,2),
                  (1,-2), (1,2), (2, -1), (2,1))
    
    visited = set()
    que = deque()
    
    visited.add(start)
    sx, sy = start
    que.append((sx, sy, 0))
    
    while(que):
        x, y, step = que.popleft()
        
        if (x,y) == end:
            return step
        
        for i,j in directions:
            nx, ny = x+i, y+j
            
            if nx < 0 or nx >= N or ny <0 or ny>= N:
                continue
            if (nx, ny) in visited:
                continue
            
            n_step = step+1
            visited.add((nx,ny))
            que.append((nx, ny, n_step))
    
def main():
    N = int(input())
    
    for _ in range(N):    
        n, start, end = data_input()
        print(bfs(n,start, end))
        
main()