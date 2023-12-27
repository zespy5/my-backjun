import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


N  = int(input())

for _ in range(N):
    M = int(input())

    nodes = set()
    edges = []
    for _ in range(M):
        f, t = input().split()
        nodes.add(f)
        nodes.add(t)
        edges.append((f,t))


    node_index = {}
    
    idx = 0
    for n in nodes:
        node_index[n] = idx
        idx+=1
    
    parents = [i for i in range(len(nodes))]
    friends_num = [1]*len(nodes)

        
    def find_root(x):
        if x == parents[x]:
            return x
        
        parents[x] = find_root(parents[x])
        return parents[x]

    def union_set(x,y):
        x = find_root(x)
        y = find_root(y)
        
        if x== y:
            return
        if x < y:
            parents[y] = x
            friends_num[x] += friends_num[y]
        else:
            parents[x] = y
            friends_num[y] += friends_num[x]
    
     
    for f, t in edges:
        fr = node_index[f]
        to = node_index[t]
        
        union_set(fr,to)
        root = find_root(fr)
        
        print(friends_num[root])