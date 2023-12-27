import sys
from collections import deque

input = sys.stdin.readline


def find_setion(rows, cols, grid):
    
    directions = ((-1,-1), (-1,0), (-1,1),
                  ( 0,-1), ( 0,1),
                  ( 1,-1), ( 1,0), ( 1,1))
    
    outter_visited = set()
    sections = []
    
    def bfs(start):
        if start in outter_visited:
            return
        
        visited = set()
        que = deque()
        
        que.append(start)
        visited.add(start)
        outter_visited.add(start)
        
        while(que):
            x,y = que.popleft()
            
            for i,j in directions:
                nx, ny = x+i, y+j 
                
                if (nx < 0 or nx >= rows or
                    ny < 0 or ny >= cols):
                    continue
                
                if (nx, ny) in visited:
                    continue
                
                if grid[nx][ny] == 1:
                    que.append((nx, ny))
                    visited.add((nx,ny))
                    outter_visited.add((nx,ny))
                    
        sections.append(visited)
        
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                bfs((i,j))       
    
    return len(sections)      
                
def main():
    while(True):
        cols, rows = map(int, input().split())
        
        if cols == 0 and rows == 0:
            break
        
        grid = [list(map(int, input().split())) for _ in range(rows)]
        
        print(find_setion(rows, cols, grid))
        
    
main()