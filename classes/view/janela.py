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

        if self.contexto.arquivo.conteudo == []:

            self.contexto.arquivo.conteudo = [""]

        
        self.reserved = ["int","float","double","struct","union","char","void","if","else","return","for","while","unsigned","short"]
        
        self.macros = ["#define","#include","#pragma","#ifdef","#ifndef","#else"]

        self.tabSize = 4

        self.screenCounter = 0

        
        self.format = formating(self)
        
        self.flag_MC = False

        self.typing = ""
        
    def showPrompt(self):

        self.screen.attron(curses.color_pair(6))

        c = len(self.dftText(self.ponteiro[1]))
        
        self.screen.move(self.ponteiro[0] -self.initL,self.screenCounter+1)
        
        txt = "" 

        tmp = self.contexto.ssense.getSugestao()

        if len(tmp) > 0:
            txt = txt + tmp[0].nome
            if tmp[0].tipo == "STRUCT" or tmp[0].tipo == "METHOD":
                parametros = ", ".join(tmp[0].params)
                txt = txt+" ("+parametros+")"
            
        self.screen.addstr(txt[0:self.W-self.screenCounter-1])

        self.screen.attroff(curses.color_pair(6))

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
        
        if str(char).isalpha() or char =='.' or char =='-' or char=='>' or char =='_' or char == '#':

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

    def drawLine(self,line,Num,flag_MC):

        word = ""
        text=self.dftText(Num)
        counter = 0
        w = 0
        l = self.getWords(line+" ")

        self.screen.addstr(text)

        drawed =  0
        flag = 0
        
        
        lineCommnet = False #Detecta //
        colon = [False,False] #detecta "
        scolon = [False,False] #detecta '
        justW = False
        
        tmp = line+" "
        for j in range(0,len(tmp)):
            
            i = tmp[j]
            
            Width = self.W - len(text)
            

            #FIla de Prioridades
            
            #1 - comentario multilinha
            #2 - comentatrio de uma única linha
            #3 - "" ou ''
            #4 - detecção de palavra macro estruturas etc
            
            #flag Handling
            
            if tmp[j] == '/' and tmp[j+1] == '/' and not colon[0] and not colon[1] :
                
                lineCommnet = True
            
            if tmp[j] == '/' and tmp[j+1] == '*' and not colon[0] and not colon[1]:
                
                self.flag_MC = True
        
            if (tmp[j] == '\"') and  (not colon[0]) and (not colon[1]) and ((tmp[j-1] != '\\') if j > 0 else 1 ):
                
                colon[0],colon[1] = True,False
            
            if tmp[j] == '\''  and  (not scolon[0]) and (not scolon[1]) and ((tmp[j-1] != '\\') if j > 0 else 1 ):
                
                scolon[0],scolon[1] = True,False
            
            if self.flag_MC:
                
                flag = 1
                pass
            
            elif lineCommnet:
                
                flag = 2
            
            elif colon[0] or scolon[0]:
                
                flag = 3
            else:
                
                if flag < 4:
                    
                    if self.reserved.count(l[w]) > 0:
                        
                        flag = 4
                    
                    elif self.macros.count(l[w]) > 0:
                        
                        flag = 5
                    
                    else:
    
                        flag = 0
                    
                
            #update da palavra
            if not self.breakWord(i):
                
                w = w+1
                
                if flag >= 4:
                    
                    flag = 0
                
            if flag == 1 or flag == 2:
                
                self.screen.attron(curses.color_pair(4))
            
            elif flag == 3:
                
                self.screen.attron(curses.color_pair(5))
            
            elif flag == 4:
                
                self.screen.attron(curses.color_pair(3))
            
            elif flag == 5:
                
                self.screen.attron(curses.color_pair(6))
                
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

            if flag == 1 or flag == 2:
                
                self.screen.attroff(curses.color_pair(4))
            
            elif flag == 3:
                
                self.screen.attroff(curses.color_pair(5))
            
            elif flag == 4:
                
                self.screen.attroff(curses.color_pair(3))
            
            elif flag == 5:
                
                self.screen.attroff(curses.color_pair(6))
            
            
            #desable flags
            
            if j > 0 and tmp[j-1] == '*' and tmp[j] == '/':
                
                self.flag_MC = False
                
            if tmp[j] == '\"' and ((tmp[j-1] != '\\') if j > 0 else 1 ):
                
                if colon[0]  and not colon[1]:
                    
                    colon[1] = True
                
                elif colon[0] and colon[1] :
                    
                    colon[0], colon[1] = False,False
            
            if tmp[j] == '\'' and ((tmp[j-1] != '\\') if j > 0 else 1 ):
                
                if scolon[0]  and not scolon[1]:
                    
                    scolon[1] = True
                
                elif scolon[0] and scolon[1] :
                    
                    scolon[0], scolon[1] = False,False
                    
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
 
    def fix_Flag_MC(self):
        
        for i in self.contexto.arquivo.conteudo[0:self.initL]:
            
            for j in range(1,len(i)):
                
                if i[j] == '*' and i[j-1] == '/':
                    
                    self.flag_MC = True
                elif i[j] == '/' and i[j-1] == '*':
                    self.flag_MC = False
                    
    def drawEditor(self):
        self.screen.move(0,0)

        #curses.curs_set(0)
        self.H,self.W = self.screen.getmaxyx()

        self.updCounter()

        #Scrool
        self.scrool()           
        self.fix_Flag_MC()
        counter = self.initL+1
        for i in self.contexto.arquivo.conteudo[self.initL:self.initL+self.H-1]:

            self.drawLine(i,counter,self.flag_MC)

            if counter <= self.initL+self.H - 1:
                self.screen.addch('\n')
            counter = counter + 1

        self.showPrompt()
        
        self.screen.refresh(0, 0, 0, 0, self.H, self.W)
      
        self.contexto.ponteiro = self.ponteiro
                    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        
class formating:
    
    def __init__(self,editor:Janela):
        
        self.editor = editor
        
    def addChar(self,char):

        self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]] = self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]][:self.editor.ponteiro[1]]+str(char)+self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]][self.editor.ponteiro[1]:]
        self.editor.ponteiro[1] = self.editor.ponteiro[1]+1

        if char.isalpha():

            self.editor.typing = self.editor.typing+char

        else:

            self.editor.typing = ""
    
    def fixInitC(self):

        ofs = 0;
        
        for i in self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]][self.editor.initC:self.editor.ponteiro[1]+1]:
            
            if i == '\t':
                
                ofs = ofs + self.editor.tabSize
                
            else:
            
                ofs = ofs + 1
                
        W = self.editor.W-len(self.editor.dftText(self.editor.ponteiro[0]))
        
        if self.editor.ponteiro[1]-self.editor.initC < 0 or ofs >= W:
            
            if self.editor.ponteiro[1] > 0:
                self.editor.initC = self.editor.ponteiro[1] - 1 
            else:
                self.editor.initC = 0

    def addLine(self):

        #tab count

        c = 0

        for i in self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]]:
            if i == '\t':
                c = c+1
            else:
                break
        subStr = ('\t'*c) + self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]][self.editor.ponteiro[1]:]

        self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]] = self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]][:self.editor.ponteiro[1]]

        if(len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]]) == 0):
            self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]] = ""
        self.editor.ponteiro[0] = self.editor.ponteiro[0]+1
        self.editor.contexto.arquivo.conteudo.insert(self.editor.ponteiro[0],subStr)
        self.editor.ponteiro[1]=c

        if c > 0:
            self.editor.initC = c - 1
        else:
            self.editor.initC = 0
        

    def nextLine(self):
        if self.editor.ponteiro[0] < len(self.editor.contexto.arquivo.conteudo)-1:

            self.editor.ponteiro[0] = self.editor.ponteiro[0]+1

        if self.editor.ponteiro[1] >= len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]]):
            
            self.editor.ponteiro[1] = len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]])
            
        self.fixInitC()
        
    def backLine(self):
        
        if self.editor.ponteiro[0] > 0:
            self.editor.ponteiro[0] = self.editor.ponteiro[0]-1
            x = self.editor.ponteiro[0]
        
        if self.editor.ponteiro[1] >= len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]]):    
            self.editor.ponteiro[1] = len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]])
            
        self.fixInitC()

    def backChar(self):
        if self.editor.ponteiro[1] > 0:
        
            self.editor.ponteiro[1] = self.editor.ponteiro[1] - 1
            
    def nextChar(self):
        if self.editor.ponteiro[1] < len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]]):
            self.editor.ponteiro[1] = self.editor.ponteiro[1] + 1
    def removeChar(self):

        subStr = self.editor.contexto.arquivo.conteudo[:self.editor.ponteiro[0]]


        if len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]])>0 and self.editor.ponteiro[1] > 0:
            self.editor.ponteiro[1] = self.editor.ponteiro[1] - 1
            self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]] = self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]][:self.editor.ponteiro[1]] + self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]][self.editor.ponteiro[1]+1:] 
            
        else:
            
            if len(self.editor.contexto.arquivo.conteudo) > 0:
                
                if self.editor.ponteiro[0] > 0:
                    tmp = self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]]

                    l = len(self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]-1])

                    self.editor.contexto.arquivo.conteudo.pop(self.editor.ponteiro[0])

                    self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]-1] = self.editor.contexto.arquivo.conteudo[self.editor.ponteiro[0]-1] + tmp

                    self.editor.ponteiro[0] = self.editor.ponteiro[0]-1

                    self.editor.ponteiro[1] = l

        if self.editor.typing != "":

            self.editor.typing = self.editor.typing[0:-1]
        
        self.editor.screen.clear()
