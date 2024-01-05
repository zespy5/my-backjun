import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

rows, cols = map(int, input().split())

paint = [[*map(int, input().split())] for _ in range(rows)]

directions = ((1,0), (0,1),(-1,0),(0,-1))

aera = 0

def dfs(x,y):
    if not paint[x][y]:
        return

    global aera
    paint[x][y] = 0
    aera += 1
    
    for i,j in directions:
        if 0<=x+i<rows and 0<=y+j<cols:
            dfs(x+i,y+j)
            
    return

num_aeras = 0
largest_aera = 0
for i in range(rows):
    for j in range(cols):
        aera = 0
        dfs(i,j)
        if aera > 0:
            num_aeras +=1
            if aera > largest_aera:
                largest_aera = aera
            
print(num_aeras)
print(largest_aera)
        