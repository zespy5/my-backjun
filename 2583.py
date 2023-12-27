import sys
from collections import deque

input = sys.stdin.readline

def data_input():
    rows, cols, times = map(int, input().split())
    
    squares = [list(map(int, input().split())) for _ in range(times)]
    
    return rows, cols, times, squares
    
def convert(square):
    rr = square[1], square[3]
    cr = square[0], square[2]
    return rr, cr

def draw_table(rows, cols, squares):
    table = [[0]*cols for _ in range(rows)]
    
    points = set()
    
    for i in squares:
        rr, cr = convert(i)
        for x in range(rr[0],rr[1]):
            for y in range(cr[0],cr[1]):
                points.add((x,y))
                
    for k in points:
        x,y = k
        table[x][y] = 1
    
    return table

def make_section(rows, cols, table):
    
    outer_visited = set()
    sections = []
    zero_p = []
    for i in range(rows):
        for j in range(cols):
            if table[i][j]==0:
                zero_p.append((i,j))
    
    def bfs(start):
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        inner_visited = set()
        que = deque()
        inner_visited.add(start)
        outer_visited.add(start)
        que.append(start)
        
        while(que):
            x,y = que.popleft()
            
            for i,j in directions:
                nx, ny = x+i, y+j
                
                if nx < 0 or nx >= rows or ny <0 or ny>= cols:
                    continue
                
                if (nx, ny) in inner_visited:
                    continue
                
                if table[nx][ny] == 1:
                    continue
                
                que.append((nx, ny))
                inner_visited.add((nx,ny))
                outer_visited.add((nx,ny))
                
        sections.append(inner_visited)
        
    for i in zero_p:
        if i not in outer_visited:
            bfs(i)
            
    answers = []
    for s in sections:
        answers.append(len(s))

    
    return answers
    
    
    
def main():
    rows, cols, times, squares = data_input()
    
    table = draw_table(rows, cols, squares)
    
    answer = make_section(rows, cols, table)
    
    answer = sorted(answer)
    
    print(len(answer))
    
    for i in answer:
        print(i, end=' ')        
main()
    
    