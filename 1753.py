import sys
from collections import defaultdict
from queue import PriorityQueue

INF = 999999

input= sys.stdin.readline
graph = defaultdict(list)

def data_input():
    nodes, edges = map(int, input().split())
    
    start = int(input())
    
    for _ in range(edges):
        u,v,w = map(int, input().split())
        u-=1
        v-=1
        graph[u].append((v,w))
        
    return nodes, start

def dijkstra(start, nodes):
    table = [INF]*nodes
    pq = PriorityQueue()
    pq.put((0,start))
    table[start] = 0
    
    
    while not pq.empty():
        now_weight, now_position = pq.get()
        
        for v, w in graph[now_position]:
            next_weight = now_weight + w
            if table[v] > next_weight:
                table[v] = next_weight
                pq.put((next_weight, v))

        
    return table    

def main():
    nodes, start = data_input()
    table = dijkstra(start-1, nodes)
    
    
    for i in table:
        if i != INF:
            print(i)
        else:
            print('INF')
            
main()