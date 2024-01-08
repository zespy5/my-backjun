import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

nodes = []

while(1):
    try:
        nodes.append(int(input()))
    except:
        break
    

def post(s,e):
    if s>e:
        return
    mid = e+1
    
    for i in range(s+1,e+1):
        if nodes[s] < nodes[i]:
            mid=i
            break
    
    post(s+1,mid-1)
    post(mid,e)
    print(nodes[s])
    
post(0,len(nodes)-1)