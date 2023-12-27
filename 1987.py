import sys
from collections import deque

def data_input():
    rows, cols = map(int, input().split())
    
    grid = [list(input().rstrip()) for _ in range(rows)]
    
    return rows, cols, grid

def bfs(rows, cols, grid):
    
    directions= ((1,0), (0,1), (-1,0),(0,-1))
    
    que = deque()
    que.append((0,0, grid[0][0]))

    
    max_step = 0
    
    while(que):
        x,y,visited = que.popleft()
        step = len(visited)
        if step > max_step:
            max_step = step
            
        for i,j in directions:
            nx, ny = x+i, y+j
            
            if nx < 0 or nx >= rows or ny <0 or ny >= cols:
                continue
            
            if grid[nx][ny] not in visited:
                next_visited = visited+grid[nx][ny]
                que.append((nx,ny, next_visited))
            
    
    return max_step

def main():
    rows, cols, grid = data_input()
    
    print(bfs(rows,cols, grid))
    
main()