import sys

input = sys.stdin.readline

INF = 9999999

N, M, K, X = map(int, input().split())

table = [[INF]*N for _ in range(N)]

for i in range(N):
    table[i][i] = 0
    
for _ in range(M):
    a,b = map(int, input().split())
    a,b = a-1, b-1
    table[a][b] = 1
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            table[i][j] = min(table[i][k]+table[k][j], table[i][j])

answer = []
for i in range(N):
    if table[X-1][i] == K:
        answer.append(i)

if answer:        
    for x in answer:
        print(x+1)
else:
    print(-1)