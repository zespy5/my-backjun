import sys
from queue import PriorityQueue as PQ

INF = 999999

grid = []
direction = ((1,0),(0,1),(-1,0),(0,-1))
minimum = 99999
table = {}

def data_input():
    rows, cols = map(int, sys.stdin.readline().split())
    wall = ['0']*(cols+2)
    
    grid.append(wall)
    for _ in range(rows):
        inst = ['0'] + list(sys.stdin.readline().rstrip()) +['0']
        grid.append(inst)
    grid.append(wall)
    
    for i in range(rows+2):
        for j in range(cols+2):
            table[(i, j)] = INF
            
    return rows, cols

def Dijkstra():
    pq = PQ()
    now_position = (1,1)
    now_step = 1
    
    pq.put((now_step, now_position))
    
    
    while(not pq.empty()):
        now_step, now_position = pq.get()
        table[now_position] = now_step
        
        for x,y in direction:
            next_position = (now_position[0]+x, now_position[1]+y)
            if grid[next_position[0]][next_position[1]] == '0':
                continue
            
            next_step = now_step+1
            if table[next_position] > next_step:
                table[next_position] = next_step
                pq.put((next_step, next_position))
            

def main():
    rows, cols = data_input()
    Dijkstra()
    print(table[(rows, cols)])

    
main()