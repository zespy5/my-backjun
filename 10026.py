import sys
from collections import deque

input = sys.stdin.readline

directions = ((1,0),(0,1),(-1,0),(0,-1))


def data_input():
    N = int(input())
    
    grid = []
    
    for _ in range(N):
        row = list(input().rstrip())
        grid.append(row)
        
    return N, grid

def find_section(N, grid):
    
    outer_visited = set()
    section = []
    
    def bfs(start):
        if start in outer_visited:
            return
        
        x,y = start
        start_color = grid[x][y]
        visited = set()
        que = deque()
        
        visited.add(start)
        outer_visited.add(start)
        que.append(start)
        
        while(que):
            now_x, now_y = que.popleft()
            
            for i,j in directions:
                n_x, n_y = now_x+i, now_y+j
                if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                    continue
                if (n_x, n_y) in visited:
                    continue
                if grid[n_x][n_y] == start_color:
                    visited.add((n_x, n_y))
                    outer_visited.add((n_x, n_y))
                    que.append((n_x, n_y))
        
        section.append(visited)
    
    for i in range(N):
        for j in range(N):
            bfs((i,j))   
            
    return section     


def main():
    N, grid = data_input()
    
    for_normal_section = find_section(N, grid)
    
    for_sackyac_grid = [['B']*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 'B':
                for_sackyac_grid[i][j] = 'R'
                
    for_sackyac_section = find_section(N, for_sackyac_grid)
    
    print(len(for_normal_section), len(for_sackyac_section))
    
main()