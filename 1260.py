from collections import defaultdict, deque

def inp():
    nodes, edges, start = map(int, input().split())
    
    graph = defaultdict(list)
    for i in range(edges):
        f, t = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)
        
    for key , values in graph.items():
        values.sort()
        
    return start, graph

def dfs(start, graph):
    answer = [start]
    stack = [start]
    visited = set([start])
    now=start
    is_end = False
    while(stack):
        for n in graph[now]:
            if not n in visited:
                is_end= False
                stack.append(n)
                break
            is_end=True
            
        if is_end:
            stack.pop()
        
        if stack:
            now = stack[-1]
            
        if not now in visited:
            answer.append(now)
        visited.add(now)
        
               
    return answer

def bfs(start, graph):
    answer = [start]
    queue = deque([start])
    visited = set([start])
    
    now=start
    while(queue):
        queue.popleft()
        
        for n in graph[now]:
            if (not n in visited) and (not n in queue):
                queue.append(n)
        if not queue:
            break
        now = queue[0]
        visited.add(now)
        answer.append(now)
    return answer
    
    
def main():
    start, graph = inp()
    da = dfs(start, graph)
    ba = bfs(start, graph)
    print(' '.join(map(str, da)))
    print(' '.join(map(str, ba)))
    
main()
    