from src.view.keylistener import KeyListener,Keys
from src.view.janela import Janela
from src.controller.contexto import Contexto
from src.controller.appcontext import AppContext

class Interface:
    '''
    Classe da interface principal do app, que suportará janelas.
    '''
    def __init__(self, listContextos, appContext : AppContext):
        self.app = appContext
        self.keylistener = KeyListener(self)
        self.janelas = []
        self.janelaAtiva = -1
        self.contextos = listContextos
        for contexto in listContextos:
            self.criarJanela(contexto)
        

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
        self.janelas.append(Janela(cntx))
        # Depois atualiza desenho da interface?
    