import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

def AC():
    cmds = list(input().rstrip())
    numD = cmds.count('D')
    
    length = int(input())
    array = input().rstrip()
    
    if numD > length:
        print('error')
        return
    
    Deq = deque()
    
    if length > 0:
        Deq = deque(array[1:-1].split(','))
    
    
    dir = 0
    for cmd in cmds:
        if cmd == 'D':
            if not dir:
                Deq.popleft()
            else:
                Deq.pop()
        elif cmd == 'R':
            dir = not dir
                
    
    if (len(cmds)-numD)%2 ==1:
        Deq.reverse()
        
    print(f'[{",".join(Deq)}]')
    
    
for _ in range(N):
    AC()