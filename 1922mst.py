import sys
import heapq as hq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

vertex = int(input())
edge_num = int(input())

edges = []

for _ in range(edge_num):
    a,b,c = map(int, input().split())
    a,b = a-1, b-1
    hq.heappush(edges, (c,a,b))
    
parents = [i for i in range(vertex)]

def find_parent(a):
    if parents[a] == a:
        return a
    
    parents[a] = find_parent(parents[a])
    return parents[a]

cost = 0

edge_contained = 1

while edge_contained < vertex:
    v, f, t = hq.heappop(edges)
    
    fp = find_parent(f)
    tp = find_parent(t)
    
    if fp != tp:
        parents[tp] = fp
        edge_contained += 1
        cost += v
        
print(cost)
        