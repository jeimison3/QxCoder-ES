from classes.view.keylistener import Keys
from classes.controller.contexto import Contexto

import curses

from classes.controller.ssense import SSense

class Janela:
    '''
    Classe de janela administrada pela classe Interface.\n
    @param Contexto
    '''

    def __init__(self, cntx : Contexto,screen):
        self.contexto = cntx
        self.ponteiro = [0,0]

        self.ponteiro[0] = self.contexto.ponteiro[0]
        self.ponteiro[1] = self.contexto.ponteiro[1]

        self.initL = self.ponteiro[0]
        self.initC = self.ponteiro[1]
        self.screen = screen

        
        self.reserved = ["int","float","double","struct","union","char","void","if","else","return","for","while"]

        self.tabSize = 4

        self.screenCounter = 0

        self.SS = SSense(self.contexto)
        

    def showPrompt(self):

        self.screen.attron(curses.color_pair(2))

        c = len(self.dftText(self.ponteiro[1]))
        
        self.screen.move(self.H - 1,0)
        
        txt = "HINT:" + self.SS.getSugestao(trecho=self.contexto.arquivo.conteudo[self.ponteiro[0]])[0]["complemento"]
        
        self.screen.addstr(txt)

        self.screen.attroff(curses.color_pair(2))

    def writeRequest(self):

        self.contexto.save()
    def updCounter(self):

        self.screenCounter=len(self.dftText(self.ponteiro[1]))

        for i in range(self.initC,self.ponteiro[1]):

            if self.contexto.arquivo.conteudo[self.ponteiro[0]][i]=='\t':

                self.screenCounter = self.screenCounter + self.tabSize

            else:
                
                self.screenCounter = self.screenCounter + 1   
                
    def keyPress(self, key : chr):
        pass
    
    def breakWord(self,char):
        
        if str(char).isalpha() or char =='.' or char =='-' or char=='>' or char =='_':

            return True

        return False
        

    def getWords(self,line):
        
        l = []

        tmp = ""

        for i in line:

            if self.breakWord(i):

                tmp = tmp + str(i)
            else:
                l.append(tmp)
                tmp = ""
        
        return l

    def drawTab(self,drawed,Width):
        self.screen.attron(2)
        for i in range(0,self.tabSize-1):
            if drawed < Width-2:
                self.screen.addch('-')
                drawed = drawed+1
        self.screen.addch('>')
        drawed = drawed+1
        self.screen.attroff(2)

        return drawed

    
    def dftText(self,lineNum):

        tmp = len(str(self.H+self.ponteiro[0]))
        text = str(lineNum)

        text = (" "*(tmp-len(text)))+text+":"

        return text

    def drawLine(self,line,Num):

        word = ""
        text=self.dftText(Num)
        counter = 0
        w = 0
        l = self.getWords(line+" ")

        self.screen.addstr(text)

        drawed =  0
        
        for i in line+" ":
            
            Width = self.W - len(text)
            

            flag1 = False

            if self.breakWord(i):
                if self.reserved.count(l[w]) > 0:
                    self.screen.attron(curses.color_pair(3))
                    flag1 = True
            else:
                w = w+1

            if counter >= self.initC and counter < self.initC + Width-1 and drawed < Width-2:
                if Num-1 == self.ponteiro[0] and counter ==  self.ponteiro[1]:
                    self.screen.attron(curses.color_pair(2))
                    if i == '\t':
                        drawed=self.drawTab(drawed,Width)
                    else:
                        self.screen.addch(i)
                        drawed = drawed + 1
                    self.screen.attroff(curses.color_pair(2))
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
        c = len(self.dftText(self.ponteiro[1]+1))
        #Scrool
        if self.ponteiro[0] - self.initL >= self.H-1:

            self.initL = self.initL + 1 

            self.screen.clear()

        if self.ponteiro[0] - self.initL < 0 and self.initL > 0:
           
            self.initL = self.initL - 1

            self.screen.clear()

        if self.screenCounter + c >= self.W:

            self.initC = self.initC + 2

            self.screen.clear()

        if self.ponteiro[1] - self.initC < 0 and self.initC > 0:

            self.initC = self.initC - 1  

            self.screen.clear()
 

    def drawEditor(self):
        self.screen.move(0,0)

        #curses.curs_set(0)
        self.H,self.W = self.screen.getmaxyx()

        self.updCounter()

        #Scrool
        self.scrool()           

        counter = self.initL+1
        for i in self.contexto.arquivo.conteudo[self.initL:self.initL+self.H-1]:

            self.drawLine(i,counter)

            if counter <= self.initL+self.H - 1:
                self.screen.addch('\n')
            counter = counter + 1

        self.showPrompt()
        
        self.screen.refresh(0, 0, 0, 0, self.H, self.W)
      
        self.contexto.ponteiro = self.ponteiro
                    
    def addChar(self,char):

        self.contexto.arquivo.conteudo[self.ponteiro[0]] = self.contexto.arquivo.conteudo[self.ponteiro[0]][:self.ponteiro[1]]+str(char)+self.contexto.arquivo.conteudo[self.ponteiro[0]][self.ponteiro[1]:]
        self.ponteiro[1] = self.ponteiro[1]+1
    
    def fixInitC(self):

        ofs = 0;
        
        for i in self.contexto.arquivo.conteudo[self.ponteiro[0]][self.initC:self.ponteiro[1]+1]:
            
            if i == '\t':
                
                ofs = ofs + self.tabSize
                
            else:
            
                ofs = ofs + 1
                
        W = self.W-len(self.dftText(self.ponteiro[0]))
        
        if self.ponteiro[1]-self.initC < 0 or ofs >= W:
            
            if self.ponteiro[1] > 0:
                self.initC = self.ponteiro[1] - 1 
            else:
                self.initC = 0

    def addLine(self):

        #tab count

        c = 0

        for i in self.contexto.arquivo.conteudo[self.ponteiro[0]]:
            if i == '\t':
                c = c+1
            else:
                break
        subStr = ('\t'*c) + self.contexto.arquivo.conteudo[self.ponteiro[0]][self.ponteiro[1]:]

        self.contexto.arquivo.conteudo[self.ponteiro[0]] = self.contexto.arquivo.conteudo[self.ponteiro[0]][:self.ponteiro[1]]

        if(len(self.contexto.arquivo.conteudo[self.ponteiro[0]]) == 0):
            self.contexto.arquivo.conteudo[self.ponteiro[0]] = ""
        self.ponteiro[0] = self.ponteiro[0]+1
        self.contexto.arquivo.conteudo.insert(self.ponteiro[0],subStr)
        self.ponteiro[1]=c

        if c > 0:
            self.initC = c - 1
        else:
            self.initC = 0
        

    def nextLine(self):
        if self.ponteiro[0] < len(self.contexto.arquivo.conteudo)-1:

            self.ponteiro[0] = self.ponteiro[0]+1

        if self.ponteiro[1] >= len(self.contexto.arquivo.conteudo[self.ponteiro[0]]):
            
            self.ponteiro[1] = len(self.contexto.arquivo.conteudo[self.ponteiro[0]])
            
        self.fixInitC()
        
    def backLine(self):
        
        if self.ponteiro[0] > 0:
            self.ponteiro[0] = self.ponteiro[0]-1
            x = self.ponteiro[0]
        
        if self.ponteiro[1] >= len(self.contexto.arquivo.conteudo[self.ponteiro[0]]):    
            self.ponteiro[1] = len(self.contexto.arquivo.conteudo[self.ponteiro[0]])
            
        self.fixInitC()

    def backChar(self):
        if self.ponteiro[1] > 0:
        
            self.ponteiro[1] = self.ponteiro[1] - 1
            
    def nextChar(self):
        if self.ponteiro[1] < len(self.contexto.arquivo.conteudo[self.ponteiro[0]]):
            self.ponteiro[1] = self.ponteiro[1] + 1
    def removeChar(self):

        subStr = self.contexto.arquivo.conteudo[:self.ponteiro[0]]


        if len(self.contexto.arquivo.conteudo[self.ponteiro[0]])>0 and self.ponteiro[1] > 0:
            self.ponteiro[1] = self.ponteiro[1] - 1
            self.contexto.arquivo.conteudo[self.ponteiro[0]] = self.contexto.arquivo.conteudo[self.ponteiro[0]][:self.ponteiro[1]] + self.contexto.arquivo.conteudo[self.ponteiro[0]][self.ponteiro[1]+1:] 
            
        else:
            
            if len(self.contexto.arquivo.conteudo) > 0:
                
                if self.ponteiro[0] > 0:
                    tmp = self.contexto.arquivo.conteudo[self.ponteiro[0]]

                    l = len(self.contexto.arquivo.conteudo[self.ponteiro[0]-1])

                    self.contexto.arquivo.conteudo.pop(self.ponteiro[0])

                    self.contexto.arquivo.conteudo[self.ponteiro[0]-1] = self.contexto.arquivo.conteudo[self.ponteiro[0]-1] + tmp

                    self.ponteiro[0] = self.ponteiro[0]-1

                    self.ponteiro[1] = l
        
        self.screen.clear()  



    

    
