import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

result = 0
n,k = map(int, input().split())

costs = []

for _ in range(n):
    cost = int(input())
    if cost <= k:
        costs.append(cost)
    

def backtracking(now_value, point):
    global result
    if now_value > k:
        return
    if now_value==k:
        result+=1
        return
    
    for i in range(point,n):
        backtracking(now_value+costs[i],i)
    return
    
backtracking(0,0)
print(result)