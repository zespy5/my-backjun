import sys
from collections import deque, defaultdict

input = sys.stdin.readline

graph = defaultdict(list)

def data_input():
    nodes, edges = map(int, input().split())
    
    for _ in range(edges):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    return nodes

def bfs(start, table):
    que = deque()
    que.append(start)
    
    visited = set()
    
    while que:
        now = que.popleft()
        visited.add(now)
        
        for i in graph[now]:
            if i not in visited:
                que.append(i)
                visited.add(i)
                table[i] = 1
                
def main():
    nodes = data_input()
    table = [0]*(nodes+1)
    table[0] = 1
    
    sets = 0
    for i in range(nodes+1):
        if table[i] == 0:
            sets +=1
            bfs(i, table)
    
    print(sets)
    
main()