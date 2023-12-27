import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def data_input():
    N = int(input())
    
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    graph = defaultdict(list)
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                graph[i].append(j)
    
    return N, graph


def dfs(start, n, graph):
    
    visited = set()
    que = deque()
    que.append(start)
    
    while(que):
        now = que.popleft()
        
        for i in graph[now]:
            if i in visited:
                continue
            
            que.append(i)
            visited.add(i)
    
    line = [0]*n
    
    for x in visited:
        line[x] = 1
        
    return line 

def main():
    n, graph = data_input()

    table = [dfs(i, n, graph) for i in range(n)]
    
    for i in table:
        for j in i:
            print(j, end=' ')
        print()
    
main()   
    