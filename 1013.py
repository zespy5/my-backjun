import sys
import re

input = sys.stdin.readline

def data_input():
    N = int(input())
    
    lines = [input().rstrip() for _ in range(N)]
    
    return lines

def main():
    p = re.compile('(100+1+|01)+')
    
    lines = data_input()
    
    yesorno = []
    for i in lines:
        m = p.fullmatch(i)
        if m:
            yesorno.append('YES')
        else:
            yesorno.append('NO')
    
    for i in yesorno:
        print(i)
    
main()   
        