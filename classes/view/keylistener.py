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
        inp = self.interface.mainScreen.getch()
        #Verificando atalho
        if inp == curses.ascii.DC3:
            self.interface.janelas[self.interface.janelaAtiva].writeRequest()
            return 1
        elif inp == curses.ascii.ESC:
            return 0
        elif inp == curses.ascii.CAN:
            for janela in self.interface.janelas:
                janela.writeRequest()
            return 0
        elif inp == curses.KEY_RESIZE:
            self.interface.janelas[self.interface.janelaAtiva].screen.clear()
            return 1
        elif inp == curses.ascii.SO:
            self.interface.janelaAtiva = (self.interface.janelaAtiva + 1) % len(self.interface.janelas)
            self.interface.drawMainWin()
            return 1
        elif inp == curses.ascii.STX:
            self.interface.janelaAtiva = (self.interface.janelaAtiva - 1) % len(self.interface.janelas)
            self.interface.drawMainWin()
            return 1
        elif inp == curses.ascii.SI:
            self.interface.open()
            return 1



                
        if curses.ascii.isprint(inp):
            self.interface.janelas[self.interface.janelaAtiva].format.addChar(chr(inp))
        elif chr(inp) == '\n':
            self.interface.janelas[self.interface.janelaAtiva].format.addLine()
        elif chr(inp) == '\t':
            self.interface.janelas[self.interface.janelaAtiva].format.addChar(chr(inp))
        elif inp == curses.KEY_DOWN:
            self.interface.janelas[self.interface.janelaAtiva].format.nextLine()
        elif inp == curses.KEY_UP:
            self.interface.janelas[self.interface.janelaAtiva].format.backLine()
        elif inp == curses.KEY_LEFT:
            self.interface.janelas[self.interface.janelaAtiva].format.backChar()
        elif inp == curses.KEY_RIGHT:
            self.interface.janelas[self.interface.janelaAtiva].format.nextChar()
        elif inp == curses.KEY_BACKSPACE:
            self.interface.janelas[self.interface.janelaAtiva].format.removeChar()
        return 1

        

        return 1
                                       
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

