import random
from time import sleep
import os
path = os.getcwd() 

class Tile:
    def __init__(self,row,col,val,status):
        self.row = col 
        self.col = row
        self.val = val
        self.status = 'Show'   
        #self.font = loadFont("SansSerif-48.vlw")
        
    def getTile(self,x,y):
        
        #FORMAT-> tile.getTile(4,self.bposx+15+ROW*120,self.bposy+15+COL*120)
        
        r = {2:238,4:237,8:243,16:247,32:245,64:235,128:238,256:242,512:229,1024:205,2048:237}
        g = {2:228,4:224,8:178,16:149,32:124,64:88,128:207,256:209,512:193,1024:166,2048:197}
        b = {2:217,4:199,8:116,16:93,32:95,64:58,128:106,256:59,512:0,1024:0,2048:0}
        
        row = x+15+self.row*120
        col = y+15+self.col*120
        
        stroke(r[self.val],g[self.val],b[self.val])
        fill(r[self.val],g[self.val],b[self.val])
        rect(row,col,110,110,10,10,10,10)
    
        if self.val <= 64:
            if self.val <= 4:
                fill(95,88,84)
                textSize(50)
                #textFont(self.font, 50)
                text(self.val,row+40,col+75)
            elif self.val >= 4:
                if self.val == 8:
                    fill(255)
                    textSize(50)
                    #textFont(self.font, 50)
                    text(self.val,row+40,col+75)
                else: 
                    fill(255)
                    textSize(50)
                    #textFont(self.font, 50)
                    text(self.val,row+22,col+75) 
            else:
                fill(255)
                textSize(50)
                #textFont(self.font, 50)
                text(self.val,row+25,col+75)
    
        elif self.val >= 1024:
            fill(255)
            textSize(40)
        #textFont(self.font, 40)
            text(self.val,row+5,col+70)
        else:
            fill(255)
            textSize(45)
            #textFont(self.font, 45)
            text(self.val,row+13,col+72)
    
        return r[self.val],g[self.val],b[self.val]
    
class Board:
    def __init__(self,w,h,bsize):
        self.w = w
        self.h = h
        self.bsize = bsize #Size of the Board
        self.bposx = (self.w - self.bsize)/2 
        self.bposy = 100
        self.noTiles = 4
        self.points = 0
        self.container = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #Tiles on the board
        self.keyboard={UP:False,LEFT:False,RIGHT:False,DOWN:False}
        self.state = False
        self.Tiles = []
    
    def End(self):
        neighbours = [[0,1], [-1,0], [1,0], [0,-1]]
        count = 0
        valid = 0
        for row in range(4):
            for col in range(4):
                if self.container[row][col] != 0:
                    count += 1
                    for n in neighbours:
                        if 0 <= row+n[0] < 4 and 0 <= col+n[1] < 4: 
                            if self.container[row][col] == self.container[row+n[0]][col+n[1]]:
                                valid += 1
                            
        if count == 16 and valid == 0:
            stroke(250)
            fill(187,173,159)
            rect(self.bposx,self.bposy,self.bsize,self.bsize,10,10,10,10)
            textSize(50)
            fill(0)
            text("Your Score:",self.bposx+120,self.bposy+100)
            textSize(40)
            fill(250)
            text(self.points,self.bposx+210,self.bposy+150)
            textSize(50)
            fill(0)
            text("Game End!",self.bposx+120,self.bposy+230)
            textSize(30)
            text("Press Play Again.",self.bposx+130,self.bposy+275)
            return True
        else:
            return False
        
         
    def dispBoard(self):
        self.header()
        #Position of the board
        stroke(250)
        fill(187,173,159)
        rect(self.bposx,self.bposy,self.bsize,self.bsize,10,10,10,10)
        
        #tile self.container
        for row in range(0,self.noTiles):
            for col in range(0,self.noTiles):
                stroke(205,193,179)
                fill(205,193,179)
                rect(self.bposx+15+row*120,self.bposy+15+col*120,110,110,10,10,10,10)  
                 
    def header(self):
        self.footer()
        
        fill(144, 122,101)
        rect(250,10,500,73,10,10,10,10)
        textSize(50)
        fill(0)
        text("2048", self.bposx+20, 65)
        
        textSize(20)
        fill(255)
        text("Score", self.bposx+360, 54)
    
        fill(256)
        rect(self.bposx+420,22,50,50,10,10,10,10)
     
        fill(255)
        if len(str(self.points)) == 1:
            text(self.points,self.bposx+439,54)
        if len(str(self.points)) == 2:
            text(self.points,self.bposx+432,54)
        if len(str(self.points)) == 3:
            text(self.points,self.bposx+425,54)
        if len(str(self.points)) >= 4:
            textSize(18)
            text(self.points,self.bposx+422,54)  
              
        fill(144, 122,101)
        rect(785,110,140,60,10,10,10,10)
        textSize(20)
        fill(250)
        text("Play Again",805, 147)
         
    def footer(self):
        textSize(12)
        fill(0)
        text("Developed by Hashim Hayat at New York University Abu Dhabi.", self.bposx+70, 625)
        textSize(10)
        text("Introduction to Computer Science in Python by Prof. Yasir Zaki.", self.bposx+100, 640)
                                      
    def begin(self):
        nolist = [0,1,2,3]
        row_first = random.choice(nolist)
        col_first = random.choice(nolist)
        self.container[row_first][col_first] = 2
    
    def dispTiles(self):
        for row in range(4):
            for col in range(4):
                val = self.container[row][col]
                if val != 0:
                    tile = Tile(row,col,val,"Show")
                    tile.getTile(self.bposx,self.bposy)
                
                        
    def MoveUp(self):
       row = 0
       for col in range(0,4):
           if self.container[row][col]!=0 or self.container[row+1][col]!=0 or self.container[row+2][col]!=0 or self.container[row+3][col]!=0:
               if self.container[row][col] == 0:
                   while self.container[row][col] == 0:
                       self.container[row][col] = self.container[row+1][col]                     
                       self.container[row+1][col] = self.container[row+2][col]                     
                       self.container[row+2][col] = self.container[row+3][col]                     
                       self.container[row+3][col] = 0
    
           if self.container[row+1][col] ==0 and (self.container[row+2][col]!=0 or self.container[row+3][col]!=0):
                   while self.container[row+1][col] == 0:                    
                       self.container[row+1][col] = self.container[row+2][col]                     
                       self.container[row+2][col] = self.container[row+3][col]                     
                       self.container[row+3][col] = 0
    
           if self.container[row+2][col]!=0 and self.container[row+3][col]!=0:
                   while self.container[row+2][col] == 0:                                         
                       self.container[row+2][col] = self.container[row+3][col]                     
                       self.container[row+3][col] = 0
    
    def AddUp(self):
       i = 0     
       self.points     
       for j in range(0,4):         
           if self.container[i][j] == self.container[i+1][j]: 
               self.container[i][j] = self.container[i][j] + self.container[i+1][j] 
               self.points += self.container[i][j] * 2 
               self.container[i+1][j] = self.container[i+2][j] 
               self.container[i+2][j] = self.container[i+3][j] 
               self.container[i+3][j] = 0 #
            
           if self.container[i+1][j] == self.container[i+2][j]:
               self.container[i+1][j] = self.container[i+1][j] + self.container[i+2][j] 
               self.points += self.container[i+1][j] * 2 
               self.container[i+2][j] = self.container[i+3][j] 
               self.container[i+3][j] = 0 
            
           if self.container[i+2][j] == self.container[i+3][j]: 
               self.container[i+2][j] = self.container[i+2][j] + self.container[i+3][j] 
               self.points += self.container[i+2][j] * 2 
               self.container[i+3][j] = 0 
    
    def MoveDown(self):
       row = 0
       for col in range(0,4):
           if self.container[row][col]!=0 or self.container[row+1][col]!=0 or self.container[row+2][col]!=0 or self.container[row+3][col]!=0:
               if self.container[row+3][col] == 0:
                   while self.container[row+3][col] == 0:
                       self.container[row+3][col] = self.container[row+2][col]                     
                       self.container[row+2][col] = self.container[row+1][col]                     
                       self.container[row+1][col] = self.container[row][col]                     
                       self.container[row][col] = 0
    
           if self.container[row+2][col] == 0 and (self.container[row+1][col]!=0 or self.container[row][col]!=0):
                   while self.container[row+2][col] == 0:                    
                       self.container[row+2][col] = self.container[row+1][col]                     
                       self.container[row+1][col] = self.container[row][col]                     
                       self.container[row][col] = 0
    
           if self.container[row+1][col] ==0 and self.container[row][col]!=0:
                   while self.container[row+1][col] == 0:                                         
                       self.container[row+1][col] = self.container[row][col]                     
                       self.container[row][col] = 0
    
    def AddDown(self):
       i = 0     
       self.points     
       for j in range(0,4):         
           if self.container[i+3][j] == self.container[i+2][j]: 
               self.container[i+3][j] = self.container[i+3][j] + self.container[i+2][j] 
               self.points += self.container[i+3][j] * 2 
               self.container[i+2][j] = self.container[i+1][j] 
               self.container[i+1][j] = self.container[i][j] 
               self.container[i][j] = 0 
            
           if self.container[i+2][j] == self.container[i+1][j]:
               self.container[i+2][j] = self.container[i+2][j] + self.container[i+1][j] 
               self.points += self.container[i+2][j] * 2 
               self.container[i+1][j] = self.container[i][j] 
               self.container[i][j] = 0 
            
           if self.container[i+1][j] == self.container[i][j]: 
               self.container[i+1][j] = self.container[i+1][j] + self.container[i][j] 
               self.points += self.container[i+1][j] * 2 
               self.container[i][j] = 0 
    
    def MoveLeft(self):
       col = 0
       for row in range(0,4):
           if self.container[row][col]!=0 or self.container[row][col+1]!=0 or self.container[row][col+2]!=0 or self.container[row][col+3]!=0:
               if self.container[row][col] == 0:
                   while self.container[row][col] == 0:
                       self.container[row][col] = self.container[row][col+1]                     
                       self.container[row][col+1] = self.container[row][col+2]                     
                       self.container[row][col+2] = self.container[row][col+3]                     
                       self.container[row][col+3] = 0
    
               if self.container[row][col+1] == 0 and (self.container[row][col+2] != 0 or self.container[row][col+2] != 0):
                   while self.container[row][col+1] == 0:                    
                       self.container[row][col+1] = self.container[row][col+2]                     
                       self.container[row][col+2] = self.container[row][col+3]                     
                       self.container[row][col+3] = 0
    
               if self.container[row][col+2] == 0 and self.container[row][col+3] != 0:
                   while self.container[row][col+2] == 0:                                         
                       self.container[row][col+2] = self.container[row][col+3]                     
                       self.container[row][col+3] = 0
    
    def AddLeft(self): 
       j=0     
       self.points     
       for i in range(0,4):       
           if self.container[i][j] == self.container[i][j+1]:        
               self.container[i][j] = self.container[i][j]+self.container[i][j+1]             
               self.points += self.container[i][j] * 2            
               self.container[i][j+1] = self.container[i][j+2]            
               self.container[i][j+2] = self.container[i][j+3]            
               self.container[i][j+3] = 0           
    
           if self.container[i][j+1] == self.container[i][j+2]:            
               self.container[i][j+1] = self.container[i][j+1]+self.container[i][j+2]           
               self.points += self.container[i][j+1] * 2              
               self.container[i][j+2] = self.container[i][j+3]  
               self.container[i][j+3] = 0     
            
           if self.container[i][j+2] == self.container[i][j+3]:        
               self.container[i][j+2] = self.container[i][j+2]+self.container[i][j+3]      
               self.points += self.container[i][j+2] * 2            
               self.container[i][j+3] = 0 
    
    def MoveRight(self):
       j=0     
       for i in range(0,4):
           if self.container[i][j]!=0 or self.container[i][j+1]!=0 or self.container[i][j+2]!=0 or self.container[i][j+3]!=0: 
               if self.container[i][j+3]==0: 
                   while self.container[i][j+3]==0: 
                       self.container[i][j+3]=self.container[i][j+2]                     
                       self.container[i][j+2]=self.container[i][j+1]                     
                       self.container[i][j+1]=self.container[i][j]                     
                       self.container[i][j]=0               
        
           if self.container[i][j+2]==0 and (self.container[i][j+1]!=0 or self.container[i][j]!=0): 
               while self.container[i][j+2]==0: 
                   self.container[i][j+2]=self.container[i][j+1]                     
                   self.container[i][j+1]=self.container[i][j]                    
                   self.container[i][j]=0               
        
           if self.container[i][j+1]==0 and self.container[i][j]!=0: 
               while self.container[i][j+1]==0: 
                   self.container[i][j+1]=self.container[i][j]                     
                   self.container[i][j]=0
    
    def AddRight(self):
       j=0     
       self.points     
       for i in range(0,4): 
           if self.container[i][j+3]==self.container[i][j+2]:
               self.container[i][j+3]=self.container[i][j+3] + self.container[i][j+2] 
               self.points += self.container[i][j+3] * 2 
               self.container[i][j+2]=self.container[i][j+1]
               self.container[i][j+1]=self.container[i][j] 
               self.container[i][j]=0 
            
           if self.container[i][j+2]==self.container[i][j+1]: 
               self.container[i][j+2]=self.container[i][j+2]+self.container[i][j+1] 
               self.points += self.container[i][j+2] * 2 
               self.container[i][j+1]=self.container[i][j]
               self.container[i][j]=0 
            
           if self.container[i][j+1]==self.container[i][j]:
               self.container[i][j+1]=self.container[i][j+1]+self.container[i][j] 
               self.points += self.container[i][j+1] * 2
               self.container[i][j]=0    
        
game = Board(1000,700,500)
       
def setup():
    path = os.getcwd()
    size(game.w,game.h)
    background(250,248,239) 
 
def draw():
    background(250,248,239)
    game.dispBoard()
    game.dispTiles()
    
    if game.state == False:
        game.begin()
        game.state = True
    else:
        status = game.End()
        if status == True:
            #game.__init__(1000,700,500)
            pass
        
        
def keyPressed():
    # print key, keyCode
    
    if keyCode==38:
        game.keyboard[UP] = True
        game.MoveUp()         
        game.AddUp()
    elif keyCode==37:
        game.keyboard[LEFT] = True
        game.MoveLeft()         
        game.AddLeft() 
    elif keyCode==39:
        game.keyboard[RIGHT] = True
        game.MoveRight()         
        game.AddRight() 
    elif keyCode==40:
        game.keyboard[DOWN] = True
        game.MoveDown()         
        game.AddDown()

    row_indexes_with_zero = []     
    column_indexes_with_zero = []     
    
    for i in range(0,4):         
        for j in range(0,4):             
            if game.container[i][j] == 0:                 
                row_indexes_with_zero.append(i)                 
                column_indexes_with_zero.append(j)             
            if game.container[i][j] == 2048:                
                game.status = False                 
                break     
    
    if len(row_indexes_with_zero) > 1:         
        random_index = row_indexes_with_zero.index(random.choice(row_indexes_with_zero))         
        row_to_place_entry = row_indexes_with_zero[random_index]         
        column_to_place_entry = column_indexes_with_zero[random_index]        
        game.container[row_to_place_entry][column_to_place_entry] = 2     
    elif len(row_indexes_with_zero) == 1:         
        row_to_place_entry = row_indexes_with_zero[0]         
        column_to_place_entry = column_indexes_with_zero[0]        
        game.container[row_to_place_entry][column_to_place_entry] = 2 
        
def keyReleased():
    if keyCode==38:
        game.keyboard[UP] = False
    elif keyCode==40:
        game.keyboard[DOWN] = False
    elif keyCode==37:
        game.keyboard[LEFT] = False
    elif keyCode==39:
        game.keyboard[RIGHT] = False

def mouseClicked():
    if 785 < mouseX < 785+140 and 110 < mouseY < 110+60:
        game.__init__(1000,700,500)