#minimum spaning tree

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def data_input():
    v, e = map(int, input().split())
    
    edge_values = []
    
    for _ in range(e):
        f, t, value = map(int, input().split())
        if f > t:
            f, t = t, f
        edge = value,f-1,t-1
        edge_values.append(edge)
        
    edge_values.sort()
    
    return v, edge_values

def main():
    v, edge_values = data_input()
    
    
    parent = [i for i in range(v)]
    
    def find_root(x):
        if x == parent[x]:
            return x
        
        parent[x] = find_root(parent[x])
        
        return parent[x]
    
    answer = []
    
    for val, f, t in edge_values:
        if len(answer) == v-1:
            break
        
        a = find_root(f)
        b = find_root(t)
        
        if a != b:
            parent[b] = a ##중요!#
            answer.append(val)
            
    print(sum(answer))
        
main()
    