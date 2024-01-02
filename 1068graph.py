import sys

input = sys.stdin.readline

N = int(input())

parents = [*map(int, input().split())]
erased = [-1]*N
children = [0]*N

erase = int(input())

parents[erase] = -2

def find_parent(x):
    if parents[x] == -1:
        return 1
    elif parents[x] == -2:
        return 0
    
    return find_parent(parents[x])

for i in range(N):
    erased[i] = find_parent(i)
    
for i in range(N):
    if not erased[i]:
        parents[i] = -2


for i in range(N):
    if parents[i] == -1:
        continue
    elif parents[i] == -2:
        children[i] = -2
    else:
        children[parents[i]] +=1


answer = children.count(0)
print(answer)
    