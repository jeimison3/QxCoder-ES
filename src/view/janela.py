from src.view.keylistener import Keys
from src.controller.contexto import Contexto

import curses

class Janela:
    '''
    Classe de janela administrada pela classe Interface.\n
    @param Contexto
    '''

    def __init__(self, cntx : Contexto,screen):
        self.contexto = cntx
        self.ponteiro = [0,0] # L,C

        self.initL = self.ponteiro[0]
        self.initC = self.ponteiro[1]
        self.screen = screen

        self.lines = [""]

        self.reserved = ["int","float","double","struct","union","char","void"]

        self.tabSize = 4


    def keyPress(self, key : chr):
        pass
    
    def getWords(self,line):
        
        l = []

        tmp = ""

        for i in line:

            if str(i).isalpha() or i =='.' or i =='-' or i=='>' or i =='_':

                tmp = tmp + str(i)
            else:
                l.append(tmp)
                tmp = ""
        
        return l

    def drawTab(self,drawed,Width):
        self.screen.attron(2)
        for i in range(0,self.tabSize-1):
            if drawed < Width-1:
                self.screen.addch('-')
                drawed = drawed+1
        self.screen.addch('>')
        drawed = drawed+1
        self.screen.attroff(2)

        return drawed

    def drawTabNS(self,drawed,Width):
        self.screen.attron(4)
        for i in range(drawed,Width-1):
            self.screen.addch('-')
        self.screen.addch('>')
        self.screen.attroff(4)
    def drawLine(self,line,Num):

        word = ""
        
        counter = 0
        w = 0
        l = self.getWords(line+" ")

        #l = line.split(" ")
        self.screen.addstr(str(Num)+":")

        drawed =  0
        
        for i in line+" ":
            
            Width = self.W - len(str(Num)+":")
            

            flag1 = False

            if self.reserved.count(l[w]) > 0:
                self.screen.attron(curses.color_pair(3))
                flag1 = True

            if not (str(i).isalpha() or i =='.' or i =='-' or i=='>' or i =='_'):
                w = w+1
            if counter >= self.initC and counter < self.initC + Width-1 and drawed < Width:
                if Num-1 == self.ponteiro[0] and counter ==  self.ponteiro[1]:
                    if i == '\t':
                        drawed=self.drawTab(drawed,Width)
                    else:
                        self.screen.attron(curses.color_pair(2))
                        self.screen.addch(i)
                        self.screen.attroff(curses.color_pair(2))

                        drawed = drawed + 1
                else:
                    if i == '\t':
                        drawed=self.drawTab(drawed,Width)
                    else:
                        self.screen.addch(i)
                        drawed = drawed + 1
            counter = counter + 1

            if(flag1):
                self.screen.attroff(curses.color_pair(3))
    
    def scrool(self):
        
        #Scrool
        if self.ponteiro[0] - self.initL >= self.H-1:

            self.initL = self.initL + 1 

        if self.ponteiro[0] - self.initL < 0 and self.initL > 0:
           
            self.initL = self.initL - 1

        if self.ponteiro[1] - self.initC < 0 and self.initC > 0:

            self.initC = self.initC - 1

        if self.ponteiro[1] - self.initC >= self.W-len(str(self.ponteiro[1]+1)+":")-1:

            self.initC = self.initC + 1  

    def Oldscrool(self):
           #Scrool
        if self.ponteiro[0] - self.initL >= self.H-1:

            self.initL = self.initL + 1 

        if self.ponteiro[0] - self.initL < 0 and self.initL > 0:
           
            self.initL = self.initL - 1

        if self.ponteiro[1] - self.initC < 0 and self.initC > 0:

            self.initC = self.initC - 1

        if self.ponteiro[1] - self.initC >= self.W-len(str(self.ponteiro[1]+1)+":")-1:

            self.initC = self.initC + 1   

    def drawEditor(self):
        self.screen.move(0,0)

        #curses.curs_set(0)
        self.H,self.W = self.screen.getmaxyx()

        #Scrool
        self.scrool()           

        counter = self.initL+1
        for i in self.lines[self.initL:self.initL+self.H-1]:

            self.drawLine(i,counter)

            if counter <= self.initL+self.H - 1:
                self.screen.addch('\n')
            counter = counter + 1

        #self.screen.move(self.ponteiro[0]-self.initL,self.ponteiro[1]+len(str(self.ponteiro[1]+1)+":"))
        #curses.curs_set(1)
        self.screen.refresh(0, 0, 0, 0, self.H, self.W)
        
    
    
    def addChar(self,char):

        self.lines[self.ponteiro[0]] = self.lines[self.ponteiro[0]][:self.ponteiro[1]]+str(char)+self.lines[self.ponteiro[0]][self.ponteiro[1]:]
        self.ponteiro[1] = self.ponteiro[1]+1
    
    def addLine(self):

        subStr = self.lines[self.ponteiro[0]][self.ponteiro[1]:]

        self.lines[self.ponteiro[0]] = self.lines[self.ponteiro[0]][:self.ponteiro[1]]

        if(len(self.lines[self.ponteiro[0]]) == 0):
            self.lines[self.ponteiro[0]] = ""
        self.ponteiro[0] = self.ponteiro[0]+1
        self.lines.insert(self.ponteiro[0],subStr)
        self.ponteiro[1]=0
        self.initC = 0


    def nextLine(self):
        if self.ponteiro[0] < len(self.lines)-1:

            self.ponteiro[0] = self.ponteiro[0]+1

        if self.ponteiro[1] >= len(self.lines[self.ponteiro[0]]):
            
            self.ponteiro[1] = len(self.lines[self.ponteiro[0]])
        
    def backLine(self):
        
        if self.ponteiro[0] > 0:
            self.ponteiro[0] = self.ponteiro[0]-1
            x = self.ponteiro[0]
        
        if self.ponteiro[1] >= len(self.lines[self.ponteiro[0]]):    
            self.ponteiro[1] = len(self.lines[self.ponteiro[0]])

    def backChar(self):
        if self.ponteiro[1] > 0:
            self.ponteiro[1] = self.ponteiro[1] -1
    def nextChar(self):
        if self.ponteiro[1] < len(self.lines[self.ponteiro[0]]):
            self.ponteiro[1] = self.ponteiro[1] + 1
    def removeChar(self):

        subStr = self.lines[:self.ponteiro[0]]

        #self.lines = self.lines[self.ponteiro[0]:]

        if len(self.lines[self.ponteiro[0]])>0 and self.ponteiro[1] > 0:
            self.ponteiro[1] = self.ponteiro[1] - 1
            self.lines[self.ponteiro[0]] = self.lines[self.ponteiro[0]][:self.ponteiro[1]] + self.lines[self.ponteiro[0]][self.ponteiro[1]+1:] 
            
        else:
            
            if len(self.lines) > 0:
                
                if self.ponteiro[0] > 0:
                    tmp = self.lines[self.ponteiro[0]]

                    l = len(self.lines[self.ponteiro[0]-1])

                    self.lines.pop(self.ponteiro[0])

                    self.lines[self.ponteiro[0]-1] = self.lines[self.ponteiro[0]-1] + tmp

                    self.ponteiro[0] = self.ponteiro[0]-1

                    self.ponteiro[1] = l
        
        self.screen.clear()










            



    

    