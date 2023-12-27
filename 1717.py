import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


def data_input():
    n, m = map(int, input().split())
    
    return n, m

def main():
    n, m = data_input()
    
    parent = [i for i in range(n+1)]
    node_rank = [1]*(n+1)
    
    def find_root(x):
        if x == parent[x]:
            return x
        
        parent[x] = find_root(parent[x])
        
        return parent[x]
    
    def union_root(x, y):
        x = find_root(x)
        y = find_root(y)
        
        if (x != y):
            if (node_rank[x] < node_rank[y]):
                parent[x] = y
            elif node_rank[x] == node_rank[y]:
                parent[x] = y
                node_rank[x] += 1
            else:
                parent[y] = x
                
    def cmd_zero(x,y):
        union_root(x,y)
        
    def cmd_one(x,y):
        x = find_root(x)
        y = find_root(y)
        
        if x==y:
            return 'yes'
        else:
            return 'no'
        
    def execution(m):
        for _ in range(m):
            cmd, a, b = map(int, input().split())
            if cmd == 0:
                cmd_zero(a,b)
            else:
                print(cmd_one(a,b))
                
    execution(m)
    
main()