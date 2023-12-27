## TLQKf

import sys
from collections import deque

input = sys.stdin.readline
INF = 999999

def data_input():
    
    rows, cols = map(int, input().split())
    
    grid = [list(map(int, list(input().rstrip()))) for _ in range(rows)]
    
    return rows, cols, grid

def draw_3d_map(rows, cols, grid):
    first_floor = [[INF]*cols for _ in range(rows)]
    second_floor = [[INF]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                first_floor[i][j]  = -1
                second_floor[i][j] = -1
                
    map_3d = [first_floor, second_floor]
    return map_3d

def modified_bfs(rows, cols, map_3d):
    directions = ((1,0), (0,1), (-1,0), (0,-1))
    
    start_node = (0,0,0,1)
    map_3d[0][0][0] = 1
    que = deque()
    que.append(start_node)
    
    while(que):
        f, x, y, step = que.popleft()
        
        for i,j in directions:
            nx, ny = x+i, y+j
            
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            
            n_step = step + 1
            first_fv = map_3d[0][nx][ny]
            second_fv = map_3d[1][nx][ny]
            
            
            if f==0:
                if first_fv == -1:
                        que.append((1,nx,ny,n_step))
                else:
                    if first_fv > n_step:
                        map_3d[0][nx][ny] = n_step
                        que.append((0,nx,ny,n_step))
                        
            else:
                if second_fv == -1:
                    continue
                elif second_fv > n_step:
                    map_3d[1][nx][ny] = n_step
                    que.append((1,nx,ny,n_step))
                
def main():
    rows, cols, grid = data_input()
    map3d = draw_3d_map(rows, cols, grid)
    modified_bfs(rows, cols, map3d)
    
    first_efv = map3d[0][rows-1][cols-1]
    second_efv = map3d[1][rows-1][cols-1]
    
    answer = -1
    
    if first_efv != INF or second_efv != INF:
        answer = min(first_efv, second_efv)

    print(answer)
    
        
        
main()
            