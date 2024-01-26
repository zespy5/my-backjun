import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

T = int(input())

def dfs(x):
    visited[x] =1
    if not visited[parents[x]]:
        dfs(parents[x])
    return

for _ in range(T):
    N = int(input())
    
    parents = [0]+[*map(int, input().split())]
    visited = [0]*(N+1)
    
    count = 0
    for i in range(1,N+1):
        if not visited[i]:
            count+=1
            dfs(i)
    print(count)