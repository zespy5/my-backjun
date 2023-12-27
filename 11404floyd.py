import sys

input = sys.stdin.readline

INF = 99999999

N = int(input())
M = int(input())

table = [[INF]*N for _ in range(N)]

for i in range(N):
    table[i][i] = 0
    
for _ in range(M):
    s,e,v = map(int, input().split())
    s -= 1
    e -= 1
    if table[s][e] > v:
        table[s][e] = v
        
def floyd():
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                table[i][j] = min(table[i][j], table[i][k]+table[k][j])
                
floyd()

for i in range(N):
    for j in range(N):
        if table[i][j] == INF:
            table[i][j] = 0

for x in table:
    for y in x:
        print(y, end=' ')
    print()
    
    