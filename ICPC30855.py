import sys

input = sys.stdin.readline

N = int(input())

fraction = input().rstrip().split(' ')

def valid(k):
    
    stack = []
    
    for i in range(N):
        if k[i] == '(':
            stack.append('(')
            stack.append(0)
        elif k[i].isnumeric():
            if len(stack) == 0:
                stack.append(-1)
                break
            stack[-1] += 1
        elif k[i] == ')':
            if len(stack) == 0:
                stack.append(-1)
                break
            if stack[-1] == 3:
                stack.pop()
                stack.pop()
                if len(stack) != 0:
                    stack[-1] += 1
        if i != N-1 and len(stack) == 0:
            return False

    if len(stack) != 0:
        return False
    else:
        return True

def gcd(a,b):
    if b>a:
        a,b = b,a
    if b == 0:
        return a
    return gcd(b, a%b)


def operation_fra(a):
    x1,x2,y1,y2,z1,z2 = a
    
    y1,y2 = y1*z2, y2*z1
    
    x, y = x1*y2+y1*x2, x2*y2
    g = gcd(x,y)
    return x//g, y//g

num = 0

def fraction1():
    global num
    k = [1]*6
    num +=1
    
    for i in range(3):
        if fraction[num]=='(':
            a,b = fraction1()
            k[2*i], k[2*i+1] = a,b
        elif fraction[num].isnumeric():
            k[2*i] = int(fraction[num])
        
        num+=1
    
    return operation_fra(k)

if valid(fraction):
    a1, a2 = fraction1()
    print(a1,a2)
else:
    print(-1)