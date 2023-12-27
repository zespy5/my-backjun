import sys
from queue import PriorityQueue
from collections import defaultdict

INF = 999999999
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)
table = [[INF]*(N+1) for _ in range(N+1)]
node_value = [INF]*(N+1)

for _ in range(M):
    s, e, v = map(int, input().split())
    graph[s].append(e)
    if table[s][e] > v:
        table[s][e] = v
    
start, end = map(int, input().split())



def dijkstra(start):
    
    node_value[start] = 0
    
    PQ = PriorityQueue()
    PQ.put((0, start))
    
    while(not PQ.empty()):
        current_value, current_node = PQ.get()
        
        for next_node in graph[current_node]:
            next_value = current_value + table[current_node][next_node]
            
            if next_value < node_value[next_node]:
                node_value[next_node] = next_value
                PQ.put((next_value, next_node))
                

answer = dijkstra(start)
print(node_value[end])