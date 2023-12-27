import sys
from collections import deque

input = sys.stdin.readline

def data_input():
    cols, rows, heights = map(int, input().split())
    
    grid = []
    rotten = []
    for _ in range(heights):
        flate = []
        for _ in range(rows):
            row = list(map(int, input().split()))
            flate.append(row)
        grid.append(flate)
        
    for i in range(heights):
        for j in range(rows):
            for k in range(cols):
                if grid[i][j][k] == 1:
                    rotten.append((i,j,k))
                    
    return cols, rows, heights, grid, rotten

def bfs(cols, rows, heights, grid, rotten):
    
    directions = ((1,0,0),(0,1,0),(0,0,1),
                  (-1,0,0),(0,-1,0),(0,0,-1))
    
    que = deque()
    visited = set()
    
    for i,j,k in rotten:
        que.append((i,j,k,1))
        visited.add((i,j,k))
    
    max_cost = 1
    while que:
        i,j,k, cost = que.popleft()
        
        for x,y,z in directions:
            ni, nj, nk = i+x, j+y, k+z
            
            if (ni < 0 or ni >= heights or
                nj < 0 or nj >= rows or
                nk < 0 or nk >= cols):
                continue
            
            if (ni, nj, nk) in visited:
                continue
            
            if grid[ni][nj][nk] == 0:
                n_cost = cost + 1
                grid[ni][nj][nk] = n_cost
                if n_cost > max_cost:
                    max_cost = n_cost
                que.append((ni, nj, nk, n_cost))
                visited.add((ni, nj, nk))
    
    for g in grid:
        for f in g:
            if 0 in f:
                return -1
    
    return max_cost-1

def main():
    cols, rows, heights, grid, rotten = data_input()
    
    ans = bfs(cols, rows, heights, grid, rotten)
    
    print(ans)

main()                