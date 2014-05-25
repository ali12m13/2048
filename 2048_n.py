import random
import os
from msvcrt import getch


m = [['' for i in range(4)] for j in range(4)]

def pr(m):

    print ".-----.-----.-----.-----."

    for i in range(4):
        st = "|"
        for j in range(4):
            st = st + "%5s|"%(m[i][j])
    
        
        print st
        print "'-----'-----'-----'-----'"
            



ls = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def new(ls,mdc):

    if mdc == 0:
        pass
    else:
        
        if len(ls) == 0:
            pass
        elif len(ls) == 1:
            a = ls[0]
            ai = a/4
            aj = a%4
            m[ai][aj] = 2
        else:
            a = random.choice(ls)
            ls.remove(a)
            b = random.choice(ls)
            ls.remove(b)

            ai = a/4
            aj = a%4

            bi = b/4
            bj = b%4

            m[ai][aj] = 2
            m[bi][bj] = 2

def moverec(cnn,sc):
    #12
    print "moves: %5i score: %5i "%(cnn,sc)
    c = getch()
    # a or 4 <-
    # d or 6 ->
    # w or 8 up
    # s or 2 down

    if c == 'd' or c == 6:
        
        mdc = r()
    elif c == 'a' or c == 4:

        mdc = l()
    elif c == 's' or c == 2:

        mdc = dw()
    elif c == 'w' or c == 8:

        mdc = up()
    else:
        mdc = [0,0]

    return mdc

def r():
    # d or 6
    mdc = 0
    sc = 0

    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = 2-j
                x = i

                if m[x][y+1] == '':
                    m[x][y+1] = m[x][y]
                    m[x][y] = ''
                    mdc = 1

    for i in range(4):
        for j in range(3):

            y = 2-j
            x = i
                
            if m[x][y+1] == m[x][y] and m[x][y] != 0:
                m[x][y+1] = m[x][y] * 2
                if m[x][y+1] != '':
                    sc = sc + m[x][y+1]
                m[x][y] = ''
                mdc = 1

    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = 2-j
                x = i

                if m[x][y+1] == '':
                    m[x][y+1] = m[x][y]
                    m[x][y] = ''
                    mdc = 1
    return [mdc,sc]
        
def l():
    # a or 4
    mdc = 0
    sc = 0

    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = j+1
                x = i

                if m[x][j] == '':
                    m[x][j] = m[x][y]
                    m[x][y] = ''
                    mdc = 1

    for i in range(4):
        for j in range(3):

            y = j+1
            x = i
                
            if m[x][j] == m[x][y] and m[x][y] != 0:
                m[x][j] = m[x][y] * 2
                if m[x][j] != '':
                    sc = sc + m[x][j]
                m[x][y] = ''
                mdc = 1

    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = j+1
                x = i

                if m[x][j] == '':
                    m[x][j] = m[x][y]
                    m[x][y] = ''
                    mdc = 1
    return [mdc,sc]

def dw():
    # s or 2
    mdc = 0
    sc = 0
    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = i
                x = 2-j

                if m[x+1][y] == '':
                    m[x+1][y] = m[x][y]
                    m[x][y] = ''
                    mdc = 1

    for i in range(4):
        for j in range(3):

            y = i
            x = 2-j
                
            if m[x+1][y] == m[x][y] and m[x][y] != 0:
                m[x+1][y] = m[x][y] * 2
                if m[x+1][y] != '':
                    sc = sc + m[x+1][y]
                m[x][y] = ''
                mdc = 1

    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = i
                x = 2-j

                if m[x+1][y] == '':
                    m[x+1][y] = m[x][y]
                    m[x][y] = ''
                    mdc = 1
    return [mdc,sc]

def up():
    # s or 2
    md = 0
    sc = 0
    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = i
                x = j+1

                if m[j][y] == '':
                    m[j][y] = m[x][y]
                    m[x][y] = ''
                    mdc = 1

    for i in range(4):
        for j in range(3):

            y = i
            x = j+1
                
            if m[j][y] == m[x][y] and m[x][y] != 0:
                m[j][y] = m[x][y] * 2
                if m[j][y] != '':
                    sc = sc + m[i][y]
                m[x][y] = ''
                mdc = 1

    for k in range(3):
        for i in range(4):
            for j in range(3):

                y = i
                x = j+1

                if m[j][y] == '':
                    m[j][y] = m[x][y]
                    m[x][y] = ''
                    mdc = 1
    return [mdc,sc]

def crt():
    cnt = -1
    ls = []
    for i in range(4):
        for j in range(4):
            cnt = cnt+1
            if m[i][j] == '':
                ls.append(cnt)
    return ls
condi = 1          
cnn = 0
new(ls,1)

change = 0
score = 0
while condi == 1:
   
  
    if os.name == 'nt':
        os.system("CLS")
    else:
        os.system("clear")
    
    
    pr(m)
    dt = moverec(cnn,score)
    score = score + dt[1]
    change = dt[0]
    if change == 0:
        pass
    else:
        cnn = cnn +1
    ls = crt()
    new(ls,change)

    if len(ls) == 0 and change == 0:
        print "lost"
        condi = 0
    else:
        pass
