import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())
grouped = 0
visit_order = 0

def find_not_cycle():
    
    N = int(input())
    next_node = [0]+[*map(int, input().split())]
    is_visited = [0]*(N+1)
    is_finished = [0]*(N+1)
    
    def find_cycle(x):
        global grouped, visit_order
        
        visit_order += 1
        is_visited[x] = visit_order
        
        if not is_visited[next_node[x]]:
            find_cycle(next_node[x])
        elif not is_finished[next_node[x]]:
            grouped += (is_visited[x] - is_visited[next_node[x]] +1)
        
        is_finished[x] = 1
    
    for i in range(1,N+1):
        find_cycle(i)
    
    answer = N-grouped
    return answer
    
        
    
for _ in range(T):
    grouped , visit_order = 0,0
    print(find_not_cycle())
    
        
        
    