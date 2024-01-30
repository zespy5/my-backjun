import sys

INF = 99999999

input = sys.stdin.readline

N,E = map(int, input().split())

node_values = [INF]*N

edgelist = []

for _ in range(E):
    a,b,c = map(int, input().split())
    a,b = a-1,b-1
    edgelist.append((a,b,c))
    
def update():
    for a,b,c in edgelist:
        if node_values[a]== INF:
            continue
        elif node_values[b] > node_values[a]+c:
            node_values[b] = node_values[a]+c
            
node_values[0] = 0


for _ in range(N-1):
    update()

lastiter = node_values[:]
update()

if lastiter == node_values:
    for i in range(1,N):
        if lastiter[i]== INF:
            print(-1)
        else:
            print(lastiter[i])
else:
    print(-1)