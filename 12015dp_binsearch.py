import sys

input = sys.stdin.readline


N = int(input())

array = [*map(int, input().split())]

increase = []

def binary_search(x):
    low = 0
    high = len(increase)-1
    mid = 0
    
    while(low<high):
        mid = low + (high - low)//2
        
        if increase[mid] >= x:
            high = mid
        else:
            low = mid + 1
    
    return high
        
increase.append(array[0])
for x in range(1,N):
    if increase[-1] < array[x]:
        increase.append(array[x])
    else:
        idx = binary_search(array[x])
        increase[idx] = array[x]
            
print(len(increase))

