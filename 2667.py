import sys
from collections import defaultdict

direction = ((1,0),(0,1),(-1,0),(0,-1))
grid =[]
already_visited = set()
def data_input():
    map_size = int(sys.stdin.readline())
    wall = ['0']*(map_size+2)
    grid.append(wall)
    
    for _ in range(map_size):
        line = ['0'] + list(sys.stdin.readline().rstrip()) + ['0']
        grid.append(line)
        
    grid.append(wall)

            
    return map_size
            

def dfs(position, visited):
    V = visited
    if grid[position[0]][position[1]] == '0':
        return V
    
    if position in visited:
        return V
    
    V.add(position)
    already_visited.add(position)
    
    for x,y in direction:
        np = (position[0]+x, position[1]+y)
        V = dfs(np, V)
        
    return V
    
    
def main():
    map_size = data_input()
    danzi = []

    for i in range(map_size+2):
        for j in range(map_size+2):
            if (i,j) not in already_visited and grid[i][j]=='1':
                visited = set()
                s=dfs((i,j), visited)
                danzi.append(s)
                
    print(len(danzi))
    answer = []
    for i in danzi:
        answer.append(len(i))
        
    answer.sort()
    for i in answer:
        print(i)
        
main()