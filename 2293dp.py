import sys


input = sys.stdin.readline

n,k = map(int, input().split())
table = [0]*(k+1)
costs = []
table[0]=1
for _ in range(n):
    cost = int(input())
    if cost <= k:
        costs.append(cost)

for i in range(len(costs)):
    for j in range(costs[i],k+1):
        table[j] += table[j-costs[i]]

print(table[k])