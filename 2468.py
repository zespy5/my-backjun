import sys
from collections import deque

input = sys.stdin.readline

def data_input():
    N = int(input())
    
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    max_height = max(max(row) for row in grid)
    
    return N, grid, max_height

def find_sections(threshold, N, grid):
    
    directions = ((1,0), (0,1), (-1,0), (0,-1))
    
    outter_visited = set()
    sections = []
    
    def bfs(start):
        if start in outter_visited:
            return
        
        visited = set()
        que = deque()
        
        visited.add(start)
        que.append(start)
        
        while(que):
            x, y = que.popleft()
            
            for i, j in directions:
                nx, ny = x+i, y+j
                
                if (nx < 0 or nx >= N or
                    ny < 0 or ny >= N):
                    continue
                
                if (nx, ny) in visited:
                    continue
                
                if grid[nx][ny] > threshold:
                    que.append((nx, ny))
                    visited.add((nx,ny))
                    outter_visited.add((nx, ny))
        
        sections.append(visited)
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] > threshold:
                bfs((i,j))
    
    return len(sections)

def main():
    N, grid, max_height = data_input()
    
    max_section = 0
    for i in range(max_height+1):
        s = find_sections(i, N, grid)
        if s > max_section:
            max_section = s
            
    print(max_section)
    
main()