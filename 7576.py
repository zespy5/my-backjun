import sys
from queue import PriorityQueue
INF = 999999
input_grid = []

def data_input():
    starting_points = []
    cols, rows = map(int, sys.stdin.readline().split())
    wall = [-2]*(cols+2)
    input_grid.append(wall)
    for x in range(rows):
        row = list(map(int, sys.stdin.readline().split()))
        row = [i+INF if i==0 else i for i in row]
        row = [-2]+row+[-2]
        input_grid.append(row)
        ys = [i for i, value in enumerate(row) if value ==1]
        for y in ys:
            starting_points.append((x+1,y))
    input_grid.append(wall)
    
    return starting_points
    
                
def make_dijkstra_table(start_points):
    
    directions = ((1,0),(0,1),(-1,0),(0,-1))
    

    PQ = PriorityQueue()
    for sp in start_points:
        PQ.put((1, sp))
    
    while(not PQ.empty()):
        now_c, now_p = PQ.get()
        
        for d in directions:
            x, y = now_p[0]+d[0], now_p[1]+d[1]
            next_p = x,y
            if input_grid[x][y] > 0:
                next_c = now_c +1
                if input_grid[x][y] > next_c:
                    input_grid[x][y] = next_c
                    PQ.put((next_c, next_p))
                    
    m = 0
    for i in input_grid:
        for j in i:
            if j == INF:
                print(-1)
                return
            if j > m:
                m = j
    
    print(m-1)
                

    
                
def main():
    starting_points= data_input()
    
    make_dijkstra_table(starting_points)

main()