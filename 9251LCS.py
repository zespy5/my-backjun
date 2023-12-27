import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s1_len = len(s1)
s2_len = len(s2)

table = [[0]*(s2_len+1) for _ in range(s1_len+1)]



for i in range(1,s1_len+1):
    for j in range(1,s2_len+1):
        if s1[i-1] == s2[j-1]:
            table[i][j] = table[i-1][j-1]+1
        else:
            table[i][j] = max((table[i-1][j], table[i][j-1]))

print(table[-1][-1])