import sys
import heapq as hq

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N,M = map(int, input().split())

parents = [i for i in range(N)]

heap = []

for _ in range(M):
    a,b,c = map(int, input().split())
    a,b = a-1, b-1
    hq.heappush(heap,(c,a,b))
    
def find_root(x):
    if parents[x]==x:
        return x
    parents[x] = find_root(parents[x])
    return parents[x]

cost = 0
count = 0

while(count<N-2):
    v,x,y = hq.heappop(heap)
    
    x = find_root(x)
    y = find_root(y)
    
    if x != y:
        parents[x] = y
        cost += v
        count+=1
        
print(cost)