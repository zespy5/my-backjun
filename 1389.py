import sys


INF = 999999
input = sys.stdin.readline

N,M = map(int, input().split())

table = [[INF]*N for _ in range(N)]

for _ in range(M):
    s,e = map(int, input().split())
    s,e = s-1,e-1
    
    table[s][e] = 1
    table[e][s] = 1
    
for i in range(N):
    table[i][i] = 0
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            table[i][j] = min(table[i][j], table[i][k]+table[k][j])
            

sums = [sum(line) for line in table]
m = min(sums)
print(sums.index(m)+1)