## greedy, heapq

import sys
import heapq

input = sys.stdin.readline

N = int(input())

time_tables = []

for _ in range(N):
    s,e = map(int, input().split())
    time_tables.append((s,e))

time_tables.sort()

end_times = [0]

for s,e in time_tables:
    if end_times[0] > s:
        heapq.heappush(end_times, e)
    else:
        heapq.heappop(end_times)
        heapq.heappush(end_times, e)

print(len(end_times))