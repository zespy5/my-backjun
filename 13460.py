import sys
from collections import deque

input = sys.stdin.readline

rows, cols = map(int, input().split())

table = [[*input().rstrip()] for _ in range(rows)]

redx, redy = 0,0
bluex, bluey = 0,0
holex, holey = 0,0

for i in range(rows):
    for j in range(cols):
        if table[i][j] == 'R':
            redx, redy = i,j
            table[i][j] = '.'
        elif table[i][j] == 'B':
            bluex, bluey = i,j
            table[i][j] = '.'
        elif table[i][j] == 'O':
            holex, holey = i,j
            
def moveright(redx, redy, bluex, bluey, cols = cols):
    red_fall_in_hole = False
    blue_fall_in_hole = False
    red_fix = False
    blue_fix = False
    
    table[redx][redy] = 'R'
    table[bluex][bluey] = 'B'
    
    if redy < bluey:
        #blue is in the further right position than red
        for _ in range(cols):
            #move blue
            if not blue_fix:
                
                if table[bluex][bluey+1] == '.':
                    table[bluex][bluey] = '.'
                    bluey += 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex][bluey+1] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluey += 1
                    
                else:
                    blue_fix = True
            
            #red_move
            if not red_fix:
                
                if table[redx][redy+1] == '.':
                    table[redx][redy] = '.'
                    redy += 1
                    table[redx][redy] = 'R'
                
                elif table[redx][redy+1] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redy += 1
                    
                else:
                    red_fix = True
    else:
        #opposite
        for _ in range(cols):
            #red_move
            if not red_fix:
                
                if table[redx][redy+1] == '.':
                    table[redx][redy] = '.'
                    redy += 1
                    table[redx][redy] = 'R'
                
                elif table[redx][redy+1] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redy += 1
                    
                else:
                    red_fix = True
            
            #move blue
            if not blue_fix:
                
                if table[bluex][bluey+1] == '.':
                    table[bluex][bluey] = '.'
                    bluey += 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex][bluey+1] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluey += 1
                    
                else:
                    blue_fix = True
    

    table[redx][redy] = '.'
    table[bluex][bluey] = '.'
    table[holex][holey] = 'O'
    return redx, redy, bluex, bluey, blue_fall_in_hole, red_fall_in_hole


def moveleft(redx, redy, bluex, bluey, cols = cols):
    red_fall_in_hole = False
    blue_fall_in_hole = False
    red_fix = False
    blue_fix = False
    
    table[redx][redy] = 'R'
    table[bluex][bluey] = 'B'
    
    if redy > bluey:
        #blue is in the further right position than red
        for _ in range(cols):
            #move blue
            if not blue_fix:
                
                if table[bluex][bluey-1] == '.':
                    table[bluex][bluey] = '.'
                    bluey -= 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex][bluey-1] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluey -= 1
                    
                else:
                    blue_fix = True
            
            #red_move
            if not red_fix:
                
                if table[redx][redy-1] == '.':
                    table[redx][redy] = '.'
                    redy -= 1
                    table[redx][redy] = 'R'
                
                elif table[redx][redy-1] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redy -= 1
                    
                else:
                    red_fix = True
    else:
        #opposite
        for _ in range(cols):
            #red_move
            if not red_fix:
                
                if table[redx][redy-1] == '.':
                    table[redx][redy] = '.'
                    redy -= 1
                    table[redx][redy] = 'R'
                
                elif table[redx][redy-1] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redy -= 1
                    
                else:
                    red_fix = True
            
            #move blue
            if not blue_fix:
                
                if table[bluex][bluey-1] == '.':
                    table[bluex][bluey] = '.'
                    bluey -= 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex][bluey-1] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluey -= 1
                    
                else:
                    blue_fix = True
    
    table[redx][redy] = '.'
    table[bluex][bluey] = '.'
    table[holex][holey] = 'O'     
    return redx, redy, bluex, bluey, blue_fall_in_hole, red_fall_in_hole


def moveup(redx, redy, bluex, bluey, rows = rows):
    red_fall_in_hole = False
    blue_fall_in_hole = False
    red_fix = False
    blue_fix = False
    
    table[redx][redy] = 'R'
    table[bluex][bluey] = 'B'
    
    if redx > bluex:
        #blue is in the further right position than red
        for _ in range(rows):
            #move blue
            if not blue_fix:
                
                if table[bluex-1][bluey] == '.':
                    table[bluex][bluey] = '.'
                    bluex -= 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex-1][bluey] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluex -= 1
                    
                else:
                    blue_fix = True
            
            #red_move
            if not red_fix:
                
                if table[redx-1][redy] == '.':
                    table[redx][redy] = '.'
                    redx -= 1
                    table[redx][redy] = 'R'
                
                elif table[redx-1][redy] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redx -= 1
                    
                else:
                    red_fix = True
    else:
        #opposite
        for _ in range(rows):
            #red_move
            if not red_fix:
                
                if table[redx-1][redy] == '.':
                    table[redx][redy] = '.'
                    redx -= 1
                    table[redx][redy] = 'R'
                
                elif table[redx-1][redy] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redx -= 1
                    
                else:
                    red_fix = True
            
            #move blue
            if not blue_fix:
                
                if table[bluex-1][bluey] == '.':
                    table[bluex][bluey] = '.'
                    bluex -= 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex-1][bluey] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluex -= 1
                    
                else:
                    blue_fix = True
    
    table[redx][redy] = '.'
    table[bluex][bluey] = '.'
    table[holex][holey] = 'O'  
    return redx, redy, bluex, bluey, blue_fall_in_hole, red_fall_in_hole


def movedown(redx, redy, bluex, bluey, rows = rows):
    red_fall_in_hole = False
    blue_fall_in_hole = False
    red_fix = False
    blue_fix = False
    
    table[redx][redy] = 'R'
    table[bluex][bluey] = 'B'
    
    if redx <= bluex:
        #blue is in the further right position than red
        for _ in range(rows):
            #move blue
            if not blue_fix:
                
                if table[bluex+1][bluey] == '.':
                    table[bluex][bluey] = '.'
                    bluex += 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex+1][bluey] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluex += 1
                    
                else:
                    blue_fix = True
            
            #red_move
            if not red_fix:
                
                if table[redx+1][redy] == '.':
                    table[redx][redy] = '.'
                    redx += 1
                    table[redx][redy] = 'R'
                
                elif table[redx+1][redy] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redx += 1
                    
                else:
                    red_fix = True
    else:
        #opposite
        for _ in range(rows):
            #red_move
            if not red_fix:
                
                if table[redx+1][redy] == '.':
                    table[redx][redy] = '.'
                    redx += 1
                    table[redx][redy] = 'R'
                
                elif table[redx+1][redy] == 'O':
                    table[redx][redy] = '.'
                    red_fall_in_hole = True
                    red_fix = True
                    redx += 1
                    
                else:
                    red_fix = True
            
            #move blue
            if not blue_fix:
                
                if table[bluex+1][bluey] == '.':
                    table[bluex][bluey] = '.'
                    bluex += 1
                    table[bluex][bluey] = 'B'
                    
                elif table[bluex+1][bluey] == 'O':
                    table[bluex][bluey] = '.'
                    blue_fall_in_hole = True
                    blue_fix = True
                    bluex += 1
                    
                else:
                    blue_fix = True
    
    table[redx][redy] = '.'
    table[bluex][bluey] = '.'
    table[holex][holey] = 'O'       
    return redx, redy, bluex, bluey, blue_fall_in_hole, red_fall_in_hole


move = {0: moveright, 1: movedown, 2 : moveleft, 3: moveup}

def bfs(redx, redy, bluex, bluey):
    
    minimum = 12
    
    que = deque()
    que.append((0,redx,redy,bluex,bluey))
    
    while(que):
        step, rx,ry,bx,by = que.popleft()
        for i in range(4):
            nrx, nry, nbx, nby, fihb, fihr = move[i](rx,ry,bx,by)
            
            if not fihb:
                
                if nrx == rx and nry == ry and nbx == bx and nby == by:
                    continue
                
                n_step = step + 1
            
                    
                if n_step > 10:
                    continue
                
                if n_step > minimum:
                    continue
                
                if fihr:
                    if n_step < minimum:
                        minimum = n_step
                        continue
                        
                que.append((n_step, nrx, nry, nbx, nby))
    
    return minimum

mini = bfs(redx, redy, bluex, bluey)

if mini == 12:
    print(-1)
else:
    print(mini)
