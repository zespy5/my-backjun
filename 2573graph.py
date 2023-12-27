import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

directions = ((1,0),(0,1),(-1,0),(0,-1))
rows, cols = map(int, input().split())


sea = [[*map(int, input().split())] for _ in range(rows)]

def after_an_year(rows, cols):
    
    temp_sea = [[0]*cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            temp_sea[i][j] = sea[i][j]
    
    for i in range(rows):
        for j in range(cols):
            if temp_sea[i][j] > 0:
                continue
            for a, b in directions:
                ni, nj = i+a, j+b
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                    continue
                if sea[ni][nj] == 0:
                    continue
                if temp_sea[ni][nj] > 0:
                    sea[ni][nj] -= 1
                    

def find_section(rows, cols):
    
    visited = [[0]*cols for _ in range(rows)]
    
    def dfs(start, num_section):
        x,y = start
        if sea[x][y] == 0:
            return
        
        if visited[x][y]:
            return 
        
        visited[x][y] = num_section
        
        for i,j in directions:
            nx, ny = x+i, y+j
            if nx < 0 or nx >= len(visited) or ny < 0 or ny >= len(visited[0]):
                continue
            if sea[nx][ny]:
                dfs((nx,ny), num_section)
    
    num_section = 0   
    for i in range(rows):
        for j in range(cols):
            if sea[i][j] == 0:
                continue
            if visited[i][j] == 0:
                num_section += 1
                dfs((i,j), num_section)
    
    return num_section


def find_years():
    years = 0
    num_section = 1
    while(num_section==1):
        after_an_year(rows, cols)
        years += 1
        num_section = find_section(rows, cols)
        if num_section == 0:
            return 0
        
    return years

print(find_years())