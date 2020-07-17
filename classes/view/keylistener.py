from enum import Enum
import threading

import curses
import curses.ascii

class Keys(Enum):
    KEY_ATALHO_NONE = 0,
    KEY_ATALHO_SALVAR = 1


class KeyListener:
    '''
    Classe com funções para reconhecimento de atalhos de teclado e interface geral entre teclas e janelas.
    '''
    def __init__(self, interface):
        self.interface = interface

        #thread = threading.Thread(target=keyListenerThread)
        #thread.start()
        pass

    def keyListenerThread(self):
        
        self.interface.tab.keypad(True)
    
        curses.raw()
        
        keySC = []

        while 1:   

            self.interface.drawMainWin() 
                        
            inp = self.interface.mainScreen.getch()

            #Verificando atalho
            
            if inp == curses.ascii.DC3:
                
                self.interface.janelas[self.interface.janelaAtiva].writeRequest()
            
            elif inp == curses.ascii.ESC:
                
                break
            
            elif inp == curses.ascii.CAN:
                
                self.interface.janelas[self.interface.janelaAtiva].writeRequest()
                break
                
            elif inp == curses.KEY_RESIZE:
                
                self.interface.janelas[self.interface.janelaAtiva].screen.clear()
                
                continue
            
            
            #JANELAS 
            #if inp==curses.ascii.ESC:

            #    self.interface.SELECTED = (self.interface.SELECTED+1)%3
                
            #    continue
                
                #self.interface.drawHF()
            #OP
            #if self.interface.SELECTED == self.interface.OP_SELECTED:
                
                #DIRECTIONAL KEY HANDLING
            #    if inp == curses.KEY_RIGHT:
            #        self.interface.OPTION = (self.interface.OPTION+1)%len(self.interface.ops)
            #    elif inp == curses.KEY_LEFT:
            #        self.interface.OPTION = (self.interface.OPTION-1)%len(self.interface.ops)
            #    elif chr(inp) == '\n':
            #        if self.interface.OPTION == 1:
            #            break
            #        elif self.interface.OPTION == 0:
            #            self.interface.janelas[self.interface.janelaAtiva].writeRequest()
                
                #self.interface.drawHF()
            #Tab
            #if self.interface.SELECTED == self.interface.TAB_SELECTED:

            #    if inp == curses.KEY_RIGHT:
            #        self.interface.janelaAtiva = (self.interface.janelaAtiva+1)%len(self.interface.janelas) 
            #    elif inp == curses.KEY_LEFT:
            #        self.interface.janelaAtiva = (self.interface.janelaAtiva-1)%len(self.interface.janelas) 
                
                #self.interface.drawHF()
            #WIN
            #if self.interface.SELECTED == self.interface.WIN_SELECTED:
                
            if curses.ascii.isprint(inp):
                self.interface.janelas[self.interface.janelaAtiva].addChar(chr(inp))
            elif chr(inp) == '\n':
                self.interface.janelas[self.interface.janelaAtiva].addLine()
            elif chr(inp) == '\t':
                self.interface.janelas[self.interface.janelaAtiva].addChar(chr(inp))
            elif inp == curses.KEY_DOWN:
                self.interface.janelas[self.interface.janelaAtiva].nextLine()
            elif inp == curses.KEY_UP:
                self.interface.janelas[self.interface.janelaAtiva].backLine()
            elif inp == curses.KEY_LEFT:
                self.interface.janelas[self.interface.janelaAtiva].backChar()
            elif inp == curses.KEY_RIGHT:
                self.interface.janelas[self.interface.janelaAtiva].nextChar()
            elif inp == curses.KEY_BACKSPACE:
                self.interface.janelas[self.interface.janelaAtiva].removeChar()
            
            self.interface.janelas[self.interface.janelaAtiva].drawEditor()
                                       
    def triggeredAtalho(self, atalho : Keys):
        '''
        Função para notificar interface do atalho pressionado.\n
        @param Atalho identificado
        '''
        self.interface.atalhoTrigger(atalho)

    def keyPress(self, key : chr):
        # KeyListener.keyPress > Interface.keyPress > Janela[i].keyPress
        '''
        Função para notificar interface da tecla pressionada.\n
        @param Char adicionado
        '''
        self.interface.keyPress(key)

