import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

table = [0]*(k+1)
costs = []

for _ in range(n):
    cost = int(input())
    if cost > k:
        continue
    if cost not in costs:
        costs.append(cost)

def dp(k):
    que = deque()
    
    for cost in costs:
        que.append(cost)
        table[cost] +=1
        
    while(que):
        cost = que.popleft()
        
        for n in costs:
            next_cost = cost+n
            if next_cost > k:
                continue
            if table[next_cost]==0 or table[next_cost] > table[cost]+1:
                table[next_cost] = table[cost]+1
                que.append(next_cost)
            if next_cost == k:
                return table[k]
    
    return -1

print(dp(k))
            
            
        