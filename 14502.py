import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def data_input():
    rows, cols = map(int, input().split())
    
    grid = []
    
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    
    return rows, cols, grid

def make_permu(rows, cols, grid):
    zero_positions = []     
    virus_positions = []
    wall_positions = []
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                zero_positions.append((i,j))
            elif grid[i][j] == 1:
                wall_positions.append((i,j))
            else:
                virus_positions.append((i,j))
                
    permutations = combinations(zero_positions,3)
    
    new_grids = []
        
    def make_g(new_g, pos, value):
        for i, j in pos:
            new_g[i][j] = value
    
    for a,b,c in permutations:
        new_g = [[0]*cols for _ in range(rows)]
        make_g(new_g, wall_positions, 1)
        make_g(new_g, (a,b,c), 1)
        make_g(new_g, virus_positions,2)
        new_grids.append(new_g)
        
    
    return new_grids, virus_positions

def spread_virus(virus, grid, rows, cols):
    
    directions = ((1,0), (0,1), (-1,0), (0,-1))
        
    que = deque()
    visited = set()
    
    for i in virus:
        que.append(i)
        visited.add(i)
        
    while que:
        now_i, now_j = que.popleft()
        
        for x,y in directions:
            next_i, next_j = now_i+x, now_j+y
            
            if (next_i, next_j) in visited:
                continue
                        
            if next_i < 0 or next_i >= rows or next_j < 0 or next_j >= cols:
                continue
            
            if grid[next_i][next_j] == 0:
                que.append((next_i, next_j))
                visited.add((next_i, next_j))
                grid[next_i][next_j] = 2

    count_zero = 0        
    for row in grid:
        count_zero += row.count(0)
    
    return count_zero


def main():
    rows, cols, grid = data_input()
    new_grids, vp = make_permu(rows, cols, grid)
    
    max_zeros = 0
    
    for grid in new_grids:
        cnt = spread_virus(vp, grid, rows, cols)
        if max_zeros < cnt:
            max_zeros = cnt    
    
    print(max_zeros)
    
main()