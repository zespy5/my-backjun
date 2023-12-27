import sys
from collections import defaultdict

input = sys.stdin.readline


given = [*input().rstrip()]
explosion = input().rstrip()
bomb_len = len(explosion)
stack = []

for s in given:
    stack.append(s)
    if ''.join(stack[-bomb_len:]) == explosion:
        for _ in range(bomb_len):
            stack.pop()

if len(stack)==0:
    print('FRULA')
else:
    print(''.join(stack))