import sys

input = sys.stdin.readline

N = int(input())
end_count = 0
house = [[*map(int, input().split())] for _ in range(N)]

end = N-1, N-1

def dfs(pipe,x,y):
    global end_count,N
    
    if (x,y) == end:
        end_count += 1
        return
    

    nx, ny = x+1, y+1
    
    if pipe == 0:
        if ny == N:
            return 
        
        if ny < N and x<N and house[x][ny] == 0:
                dfs(0,x,ny)
            
        if nx < N and y< N and house[x][ny] == 0 and house[nx][y] == 0 and house[nx][ny] == 0:
                dfs(2,nx,ny)
                    
    elif pipe == 1:
        if nx == N:
            return
        
        if nx < N and y < N and house[nx][y] == 0:
                dfs(1,nx,y)
            
        if ny < N and x < N and house[nx][y] == 0 and house[x][ny] == 0 and house[nx][ny] == 0:
                dfs(2,nx,ny)
    
    else:
        if ny < N and x<N and house[x][ny] == 0:
                dfs(0,x,ny)
        
        if nx < N and y< N and house[nx][y] == 0:
                dfs(1,nx,y)
                
        if nx < N and ny < N  and house[x][ny] == 0 and house[nx][y] == 0 and house[nx][ny] == 0:
                dfs(2,nx,ny)


dfs(0,0,1)

print(end_count)
    