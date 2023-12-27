import sys
import heapq as hq

INF = 99999999

input = sys.stdin.readline

N,M,X = map(int, input().split())
X -= 1

graph_value = [[-1]*N for _ in range(N)]
graph = [[] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int, input().split())
    a,b = a-1,b-1
    graph_value[a][b] = c
    graph[a].append(b)

def djikstra(start):
    
    table = [INF]*N
    
    PQ = []
    hq.heappush(PQ, (0,start))
    table[start] = 0
    
    while(PQ):
        value, node = hq.heappop(PQ)
        
        for i in graph[node]:
            n_value = value + graph_value[node][i]
            
            if table[i] > n_value:
                table[i] = n_value
                hq.heappush(PQ,(n_value,i))
    
    return table

table = []

for i in range(N):
    table.append(djikstra(i))
    
fromtofrom = []

for i in range(N):
    fromtofrom.append(table[i][X]+table[X][i])

print(max(fromtofrom))
    
    
            
            