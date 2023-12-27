import sys

input = sys.stdin.readline

N, B = map(int, input().split())

matrix = [[*map(int, input().split())] for _ in range(N)]

def sequence(b):
    seq = []
    
    while(b!=1):
        if b % 2 == 0:
            b /= 2
            seq.append(0)
        else:
            b-=1
            seq.append(1)
    seq.reverse()
    return seq
          

def power2(m):
    n = len(m)
    
    result = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            s = 0
            for i in range(n):
                s += m[row][i]*m[i][col]
            result[row][col] = s%1000 #중요
            
    return result

def mat_mul(m1, m2):
    n = len(m1)
    
    result = [[0]*n for _ in range(n)]
    
    
    for row in range(n):
        for col in range(n):
            s = 0
            for i in range(n):
                s += m1[row][i]*m2[i][col]
            result[row][col] = s %1000
    return result


seq = sequence(B)

answer = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        answer[i][j] = matrix[i][j]
        
for x in seq:
    if x==0:
        answer = power2(answer)
    else:
        answer = mat_mul(answer, matrix)
        
for row in answer:
    for col in row:
        print(col%1000, end=' ')
    print()