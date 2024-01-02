import sys

input = sys.stdin.readline

N = int(input())

parents = [i for i in range(N)]

M = int(input())

graph = [[*map(int, input().split())] for _ in range(N)]

schedule = [*map(int, input().split())]

for i in range(M):
    schedule[i] -= 1
    

def find_parents(a):
    if a == parents[a]:
        return a
    
    parents[a] = find_parents(parents[a])
    return parents[a]

def union_set(x,y):
    x = find_parents(x)
    y = find_parents(y)
    
    if x==y:
        return 

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

for i in range(N):
    for j in range(i,N):
        if graph[i][j]:
            union_set(i,j)
    
    
def is_ok(m):
    parent0 = find_parents(schedule[0])
    
    for x in range(1,m):
        if parent0 != find_parents(schedule[x]):
            return 'NO'
    
    return 'YES'

print(is_ok(M))