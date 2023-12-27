import sys
import heapq as hq

INF = 9999999

input = sys.stdin.readline

N, E = map(int, input().split())

graph_value = [[-1]*N for _ in range(N)]
graph = [[] for _ in range(N)]

for _ in range(E):
    a,b,c = map(int, input().split())
    a,b = a-1,b-1
    
    graph_value[a][b] = c
    graph_value[b][a] = c
    
    graph[a].append(b)
    graph[b].append(a)

bia1, bia2 = map(int, input().split())
bia1, bia2 = bia1 - 1, bia2 -1

def dijkstra(start):
    table = [INF]*N
    
    PQ = []
    hq.heappush(PQ, (0,start))
    table[start] = 0
    
    while(PQ):
        value, node = hq.heappop(PQ)
        
        for n in graph[node]:
            n_value = value + graph_value[node][n]
            
            if n_value < table[n]:
                table[n] = n_value
                hq.heappush(PQ, (n_value,n))
                
    return table

fromstart = dijkstra(0)
frombia1 = dijkstra(bia1)
frombia2 = dijkstra(bia2)

toN = min(fromstart[bia1]+frombia1[bia2]+frombia2[N-1],
          fromstart[bia2]+frombia2[bia1]+frombia1[N-1])

if toN >= INF:
    print(-1)
else:
    print(toN)
    
    
