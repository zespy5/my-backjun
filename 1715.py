import sys
import heapq

input = sys.stdin.readline

N = int(input())

decks = []
heapq.heapify(decks)

for _ in range(N):
    k = int(input())
    heapq.heappush(decks,k)

temp = heapq.heappop(decks)
result = 0

for _ in range(N-1):
    heapq.heappush(decks,temp)
    x = heapq.heappop(decks)
    y = heapq.heappop(decks)
    temp = x+y
    result += temp
    
print(result)    
    