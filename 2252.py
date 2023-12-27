import sys
from collections import deque
from queue import PriorityQueue
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

root = [i for i in range(N+1)]
node_rank = [1]*(N+1)

def find_root(x):
    if x == root[x]:
        return x
    
    root[x] = find_root(root[x])
    return root[x]

def union_set(x,y):
    x = find_root(x)
    y = find_root(y)
    
    if x != y:
        if node_rank[x]< node_rank[y]:
            root[x] = y
        elif node_rank[x]==node_rank[y]:
            root[x] = y
            node_rank[x]+=1
        else:
            root[y] = x
                
for _ in range(M):
    f, b = map(int, input().split())
    graph[b].append(f)
    union_set(f,b)
    

ranks = PriorityQueue()

def define_ranks():
    outer_visited = set()
    
    def bfs(start):
        
        inner_visited = set()
        inner_visited.add(start)
        outer_visited.add(start)
        
        que = deque()
        que.append((start, 1))
        
        while(que):
            now_node, now_rank = que.popleft()
            ranks.put((-now_rank, now_node))
            
            for next_node in graph[now_node]:
                if next_node in inner_visited:
                    continue
                
                next_rank = now_rank+1
                que.append((next_node, next_rank))
                inner_visited.add(next_node)
                outer_visited.add(next_node)
                
    for i in range(1,N+1):
        if i in outer_visited:
            continue
        
        x = find_root(i)
        bfs(x)
            
define_ranks()

while(not ranks.empty()):
    _, answer = ranks.get()
    print(answer, end=' ')
                
    
    
