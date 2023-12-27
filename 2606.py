from collections import defaultdict
import sys

graph = defaultdict(list)
visited = set([])

def data_input():
    nodes_num = int(sys.stdin.readline())
    edges_num = int(sys.stdin.readline())
    
    for _ in range(edges_num):
        a, b = sys.stdin.readline().split()
        graph[a].append(b)
        graph[b].append(a)
        
def dfs(start):
    if start in visited:
        return
    
    visited.add(start)
    for node in graph[start]:
        dfs(node)
        
    return

def main():
    data_input()
    dfs('1')
    print(len(visited)-1)
    
main()