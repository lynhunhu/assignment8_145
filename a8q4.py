#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623

class tuples(object):
    def __init__(self,r,c):
        self.__r = r
        self.__c = c
    def getRow(self):
        return self.__r
    def getColumn(self):
        return self.__c
    def setRow(self,row):
        self.__r = row
    def setColumn(self,column):
        self.__c = column
    

def isSafe(m,c,r):
    if 0<=r<=len(m) and 0<=c<len(m[0]) and m[r][c] == '0':
        return True
    return False

def DirectionMove(m,s):
    #Left
    if (int(s.getColumn())+1 <= len(m)) and (m[int(s.getRow())][int(s.getColumn())+1] == '0'):
        return 'Left'
    if int(s.getRow()+1) < len(m):
        if(m[int(s.getRow()+1)][int(s.getColumn())] == '0'):
            return 'Up'
    if ((int(s.getRow()) - 1) >= 0) :
        if(m[int(s.getRow()-1)][int(s.getColumn())] != '1'):
            return 'Down'
    return 'Right'

def SolveMaze(m,s,g):
    isdone = False
    mR = len(m) - 1
    mC = len(m[0]) - 1 
    
    if(s.getRow() > mR or s.getColumn() > mC):
        return False
    if((s.getRow() == g.getRow()) and (s.getColumn() == g.getColumn())):
        m[int(s.getRow())][int(s.getColumn())] = 'P'
        return True
   
    if((int(s.getRow()) >= 0) and (mR >= int(s.getRow())) and (int(s.getColumn()) >= 0) and (int(s.getColumn()) <= mC)):
        if((int(s.getRow())) == int(g.getRow()) and (int(s.getColumn())) == int(g.getColumn())):
            isdone = True
          
        else:
            if not isdone and  m[int(s.getRow())][int(s.getColumn())] == '0':
                m[int(s.getRow())][int(s.getColumn())] = 'P'
            d = DirectionMove(m,s)
            # print(d)
          
            # left
            if not isdone and d=='Left':
                if m[int(s.getRow())][int(s.getColumn())+1] == '0':
                    s.setColumn(int(s.getColumn())+1)
                    SolveMaze(m,s,g)
            # up
            if not isdone and d=='Up':
                if m[int(s.getRow())+1][int(s.getColumn())] == '0':
                    s.setRow(int(s.getRow())+1)
                    SolveMaze(m,s,g)
                
            # down
            if not isdone and d=='Down':
                if int(s.getRow()+1) > mR or ((int(s.getColumn()+1) > mC or  m[int(s.getRow())][int(s.getColumn())+1] == '*') and  m[int(s.getRow())+1][int(s.getColumn())] == '*'):  
                    m[int(s.getRow())][int(s.getColumn())] = '*'
                    m[int(s.getRow()-1)][int(s.getColumn())] = 'P'
                s.setRow(int(s.getRow())-1)
                SolveMaze(m,s,g)
            # right
            if not isdone and d=='Right':
                m[int(s.getRow())][int(s.getColumn())] = '*'
                s.setColumn(int(s.getColumn()) -1)
                SolveMaze(m,s,g)
    return isdone

def clearMarked(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '*':
                m[i][j] = '0'

def printMaze(m):
    for line in m:
        print(line)



## Maze 1
maze1 = []
s = tuples(0,3)
g = tuples(4,5)
with open('Maze1.txt') as f:
    content = f.read().splitlines()
for line in content:
    maze1.append(line.split())

print("Before")
for line in maze1:
    print(line)
SolveMaze(maze1,s,g)
clearMarked(maze1)
print("After")
for line in maze1:
    print(line)
    
# ## Maze 2

maze2 = []
s=tuples(0,0)
g=tuples(8,9)
with open('Maze2.txt') as f:
    content = f.read().splitlines()
for line in content:
    maze2.append(line.split())

print("Before")
for line in maze2:
    print(line)
SolveMaze(maze2,s,g)
clearMarked(maze2)
print("After")
for line in maze2:
    print(line)

