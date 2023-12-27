import sys

sys.setrecursionlimit(10000)

direction = ((1,0),(0,1),(-1,0),(0,-1))

def data_input():
    grid = []
    cols, rows, bacus = map(int, sys.stdin.readline().split())
    
    for _ in range(rows+2):
        line = [0]*(cols+2)
        grid.append(line)
        
    for _ in range(bacus):
        y, x = map(int, sys.stdin.readline().split())
        x+=1
        y+=1
        grid[x][y] = 1
        
    return rows, cols, grid


def test():
    
    rows, cols, grid = data_input()
    visited = set()
    d = []
    def dfs(p, v):
        if grid[p[0]][p[1]] == 0:
            return v
        
        if p in v:
            return v
        
        v.add(p)
        visited.add(p)
        
        for x,y in direction:
            np = p[0]+x, p[1]+y
            dfs(np,v)
        
        return v
    
    for i in range(rows+2):
        for j in range(cols+2):
            p = i,j
            if p not in visited and grid[i][j] == 1:
                v = set()
                s = dfs(p,v)
                d.append(s)
    
    print(len(d))
    
    
def main():
    test_size = int(sys.stdin.readline())
    
    for _ in range(test_size):
        test()
        
main()