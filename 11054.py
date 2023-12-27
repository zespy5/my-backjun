import sys

input = sys.stdin.readline

N = int(input())

array = [*map(int, input().split())]

largest = max(array)
largest_idx = []

for i in range(N):
    if array[i] == largest:
        largest_idx.append(i)



increase_dp = [1]*N
decrease_dp = [1]*N

for i in range(N):
    for j in range(i):
        if array[i] > array[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j]+1)
        if array[N-1-i] > array[N-1-j]:
            decrease_dp[N-1-i] = max(decrease_dp[N-1-i], decrease_dp[N-1-j]+1)
            

maximum = 0
for i in range(N):
    add = increase_dp[i]+decrease_dp[i]
    if  add > maximum:
        maximum = add
        
print(maximum-1)
        
