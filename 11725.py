import sys
from collections import defaultdict, deque

input = sys.stdin.readline



def data_input():
    N = int(input())
    
    graph = defaultdict(list)
    
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    return N, graph
        
def bfs(N, graph):
    answer = [0]*(N+1)
    visited = set()
    que = deque()
    
    visited.add(1)
    que.append((1,0))
    
    while(que):
        now, parent = que.popleft()
        
        for x in graph[now]:
            if x in visited:
                continue
            
            que.append((x,now))
            visited.add(x)
            answer[x] = now
    
    return answer

def main():
    N, graph = data_input()
    
    answer = bfs(N, graph)
    
    for i in range(len(answer)):
        if i < 2:
            continue
        print(answer[i])
        
main()
    
        