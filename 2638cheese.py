import sys

sys.setrecursionlimit(10**5)

directions= ((1,0),(0,1),(-1,0),(0,-1))

input = sys.stdin.readline

rows, cols = map(int, input().split())

dish = [[*map(int, input().split())] for _ in range(rows)]

edges = set()

def is_melt(x,y):
    count = 0
    for i,j in directions:
        nx,ny = x+i,y+j
        if dish[nx][ny]==-1:
            count+=1
    
    if count>1:
        return True
    else:
        return False

def dfs(x,y):
    if dish[x][y] == -1:
        return
    elif dish[x][y] == 1:
        edges.add((x,y))
        return
    
    dish[x][y] = -1
    
    for i,j in directions:
        nx,ny = x+i,y+j
        if 0<=nx<rows and 0<=ny<cols:
            dfs(nx,ny)

dfs(0,0)
cnt = 0
while(1):
    is_end = True
    for row in dish:
        if any(n==1 for n in row):
            is_end = False
    
    if is_end:
        print(cnt)
        break

    cnt+=1

    melting = []

    for x,y in edges:
        if is_melt(x,y):
            dish[x][y] = 0
            melting.append((x,y))
            
    '''for i in dish:
        for j in i:
            print(f"{j:>2d}",end=" ")
        print()
    print()'''

        
    edges = set()

    for x,y in melting:
        dfs(x,y)
        
    '''for i in dish:
        for j in i:
            print(f"{j:>2d}",end=" ")
        print()
    print(edges)

    for a,b in edges:
        dish[a][b] = 0

    for i in dish:
        for j in i:
            print(f"{j:>2d}",end=" ")
        print()'''
        

    


'''for i in dish:
    for j in i:
        print(f"{j:>2d}",end=" ")
    print()
print(edges)

for a,b in edges:
    dish[a][b] = 0

for i in dish:
    for j in i:
        print(f"{j:>2d}",end=" ")
    print()'''