import sys

sys.setrecursionlimit(10000)
INF = 9999999
input = sys.stdin.readline

class Node:
    def __init__(self, now, breaker):
        self.now = now
        self.visited = set()
        self.breaker = breaker
        
    def __len__(self):
        return len(self.visited)
    
    def add(self, n):
        self.visited.add(n)
        
    def print(self):
        for i in self.visited:
            print(i, end=' ') 
        print()
        
directions = ((0,1),(1,0),(0,-1),(-1,0))
grid = []
min_route = INF
rows, cols = 0, 0

def data_input():
    global rows, cols
    rows, cols = map(int, input().split())
    
    for _ in range(rows):
        row = list(map(int, list(input().rstrip())))
        grid.append(row)



def dfs(node):
    global min_route, rows, cols

    x,y = node.now
    if x == rows-1 and y == cols-1:
            if min_route > len(node):
                min_route = len(node)
            return
    
    for i,j in directions:
        able = node.breaker
        nx, ny = x+i, y+j
        if nx < 0 or nx >= rows or ny<0 or ny>=cols:
            continue
        
        if (nx, ny) in node.visited:
            continue
        
        if min_route < len(node):
            return
        
        if grid[nx][ny]==1:
            if able:
                able = False
            else:
                continue
                
        next_node = Node((nx,ny), able)
        next_node.visited = node.visited.copy()
        next_node.add((nx,ny))
        dfs(next_node)
        
    return

def main():
    data_input()
    node = Node((0,0),True)
    node.visited.add((0,0))
    dfs(node)
    if min_route== INF:
        print(-1)
    else:
        print(min_route)
    
main()
