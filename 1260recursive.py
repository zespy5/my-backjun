from collections import defaultdict, deque

graph = defaultdict(list)
dfs_visited = set([])
bfs_visited = set([])
dfs_answer = []
bfs_answer = []

def inp():
    nodes, edges, start = map(int, input().split())
    
    for i in range(edges):
        f, t = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)
        
    for _, values in graph.items():
        values.sort()
        
    return start

def dfs(node):
    if node in dfs_visited:
        return
    
    dfs_visited.add(node)
    dfs_answer.append(node)
    
    for next in graph[node]:
        dfs(next)
    return

def bfs(start):
    bfs_visited.add(start)
    bfs_answer.append(start)
    queue = deque([start])

    
    now=start
    while(queue):
        queue.popleft()
        
        for n in graph[now]:
            if (not n in bfs_visited) and (not n in queue):
                queue.append(n)
        if not queue:
            break
        now = queue[0]
        bfs_visited.add(now)
        bfs_answer.append(now)
    
    return 
    
    
def main():
    start = inp()
    dfs(start)
    bfs(start)
    print(' '.join(map(str, dfs_answer)))
    print(' '.join(map(str, bfs_answer)))
    
main()
    