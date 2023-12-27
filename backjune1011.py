import math


    
def main():
    x = int(input())
    for i in range(x):
        a, b = map(int, input().split())
        N = b-a
        k = int(math.sqrt(N))
        r = N - k**2

        if r == 0:
            print(2*k-1)
        elif r <= k:
            print(2*k)
        else:
            print(2*k+1)

main()