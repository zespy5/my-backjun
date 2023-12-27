import sys
from collections import deque

TABLENUM = 100001

def data_input():
    N, K = map(int, sys.stdin.readline().split())
    return N,K

              
def main():
    N,K = data_input()
    table = [0]*TABLENUM
    
    Que = deque()
    Que.append(N)
    
    while Que:
        now = Que.popleft()
        
        if now == K:
            break
        
        for i in now-1, now+1, now*2:
            if 0<= i < TABLENUM and table[i] == 0:
                table[i] = table[now]+1
                Que.append(i)
    
    print(table[K])
                

            
     
main()