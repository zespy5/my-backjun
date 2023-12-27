import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

rows, cols = map(int, input().split())

table = [[*map(int, input().split())] for _ in range(rows)]

movement = ((1,0), (0,1), (-1,0), (0,-1))

result = 0

def dfs(now=(0,0)):
    now_x, now_y = now
    global result
    
    for i,j in movement:
        n_x, n_y = now_x+i, now_y+j
        if  0 <= n_x < rows and 0 <= n_y < cols and table[n_x][n_y] < table[now_x][now_y]:
            if n_x==rows-1 and n_y==cols-1:
                result+=1
            dfs((n_x, n_y))
            
    return

dfs()

print(result)