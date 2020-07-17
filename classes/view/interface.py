from classes.view.keylistener import KeyListener,Keys
from classes.view.janela import Janela
from classes.controller.contexto import Contexto
from classes.controller.appcontext import AppContext

import curses
import threading
class Interface:
    '''
    Classe da interface principal do app, que suportará janelas.
    '''
    def __init__(self, listContextos, appContext : AppContext):
        self.app = appContext
        #self.keylistener = KeyListener(self)
        self.janelas = []
        self.janelaAtiva = 0
        self.contextos = listContextos
        


        #WIns
        self.mainScreen = curses.initscr() #Janela principal
        self.tab = curses.newwin(0,0,0,0)
        self.footer = curses.newwin(0,0,0,0)
        self.editor = curses.newpad(1,1)

        curses.curs_set(0)
        #SELEÇÂO
        self.TAB_SELECTED = 0
        self.OP_SELECTED = 1
        self.WIN_SELECTED = 2

        self.SELECTED = 1

        #OPÇÕES
        self.OPTION = 0
        self.ops = [" SALVAR "," FECHAR "," ABRIR "," AJUDA "]
        #CORES
        curses.start_color()

        curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)
        curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
        curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLACK)
        curses.init_pair(4,curses.COLOR_CYAN,curses.COLOR_BLACK)
        #curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_CYAN)
        curses.init_pair(5,curses.COLOR_BLACK,curses.COLOR_WHITE)
        self.COLOR_BLUE_PAIR = 3
        
        #Criando janelas
        
        for contexto in listContextos:
            self.criarJanela(contexto)
        
        #Cursor
        curses.curs_set(0)
        #Thread Keyboard
       
        self.lastPC = None
        self.lastNPC = None
        self.lastWold = None

        #self.lines = [" "]

        self.mainScreen.keypad(True)
        self.keylistener = KeyListener(self)
        #kList = threading.Thread(target=self.keylistener.keyListenerThread,name="klthread")

        self.drawMainWin()
        #kList.start()
        self.keylistener.keyListenerThread()
        
        self.mainScreen.clear()
        self.footer.clear()
        self.tab.clear()
        
        curses.endwin()
        

        

    def atalhoTrigger(self, key : Keys):
        '''
        Evento chamado a cada atalho reconhecido no KeyListener da interface
        '''

        if key == Keys.KEY_ATALHO_SALVAR:
            # Solicita à janela atual para salvar
            pass
        pass

    def keyPress(self, key : chr):
        '''
        Repasse de tecla pressionada para janela ativa
        '''
        self.janelas[self.janelaAtiva].keyPress(key)

    def criarJanela(self, cntx : Contexto):
        self.janelas.append(Janela(cntx,self.editor))
        # Depois atualiza desenho da interface?
    
    def drawMainWin(self):


        self.mainScreen.move(0,0)
        #self.footer.move(0,0)
        self.tab.move(0,0)

        #Iniciando - Verificando erros de tamanho        
        Height,Width = self.mainScreen.getmaxyx()
        

        
        #header
        self.tab.resize(1,Width)
    
        self.tab.mvwin(Height-1,0)
        
        
        #-------------------------------FOOTER
        #self.footer.resize(1,Width)        
        
        #self.footer.mvwin(Height-1,0)
        

        #footerSize = 0

        #for i in self.ops:

        #    footerSize = footerSize + len(i)

        #if self.SELECTED != self.OP_SELECTED:

        #    for i in self.ops:

        #        self.footer.addstr(i)
        #else:
        #    counter = 0
        #    for i in self.ops:

        #        if counter == self.OPTION:
        #            self.footer.attron(curses.color_pair(2))
        #            self.footer.addstr(i)
        #            self.footer.attroff(curses.color_pair(2))
        #        else:
        #            self.footer.addstr(i)
        #        counter = counter + 1
        #TAB
        #self.tab.move(0,0)
        #if self.SELECTED == self.TAB_SELECTED:
            #self.tab.attron(curses.color_pair(2))
        #    self.tab.addstr("*"+self.janelas[self.janelaAtiva].contexto.arquivo.local,Width-1)
            #self.tab.attroff(curses.color_pair(2))
        #else:
        #    self.tab.addstr(self.janelas[self.janelaAtiva].contexto.arquivo.local,Width-1)



       
        
        self.tab.addstr(self.janelas[self.janelaAtiva].contexto.arquivo.local,Width-1)
        self.mainScreen.refresh()
        #self.footer.refresh()
        self.tab.refresh()
        #self.editor.refresh(0, 0, 0, 0, Height, Width)
        #Editor
        self.editor.resize(Height-1,Width)
        self.janelas[self.janelaAtiva].drawEditor()
        #Curso on
        #curses.curs_set(1)
    
    def drawHF(self):
        
        self.footer.move(0,0)
        self.footer.clear()
        self.tab.clear()

       

        #Iniciando - Verificando erros de tamanho        
        Height,Width = self.mainScreen.getmaxyx()
        

        
        #header
        self.tab.resize(1,Width)
    
        self.tab.mvwin(Height-2,0)
        
        
        #-------------------------------FOOTER
        #self.footer.resize(1,Width)        
        
        #self.footer.mvwin(Height-1,0)
        

        #footerSize = 0

        #for i in self.ops:
        #
        #    footerSize = footerSize + len(i)

        #if self.SELECTED != self.OP_SELECTED:

        #    for i in self.ops:

        #        self.footer.addstr(i)
        #else:
        #    counter = 0
        #   for i in self.ops:
        #
        #       if counter == self.OPTION:
        #           self.footer.attron(curses.color_pair(2))
        #            self.footer.addstr(i)
        #            self.footer.attroff(curses.color_pair(2))
        #        else:
        #            self.footer.addstr(i)
        #        counter = counter + 1
        #TAB
        #self.tab.move(0,0)
        #if self.SELECTED == self.TAB_SELECTED:
            #self.tab.attron(curses.color_pair(2))
        #     self.tab.addstr("*"+self.janelas[self.janelaAtiva].contexto.arquivo.local,Width-1)
            #self.tab.attroff(curses.color_pair(2))
        #else:
        #    self.tab.addstr(self.janelas[self.janelaAtiva].contexto.arquivo.local,Width-1)
        self.tab.addstr(self.janelas[self.janelaAtiva].contexto.arquivo.local,Width-1)


       
        
        
        self.mainScreen.refresh()
        #self.footer.refresh()
        self.tab.refresh()
        #self.editor.refresh(0, 0, 0, 0, Height, Width)
        #Editor
        #self.editor.resize(Height-2,Width)
        #self.janelas[self.janelaAtiva].drawEditor()
        
