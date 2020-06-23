from src.view.keylistener import Keys
from src.controller.contexto import Contexto

class Janela:
    '''
    Classe de janela administrada pela classe Interface.\n
    @param Contexto
    '''

    def __init__(self, cntx : Contexto):
        self.contexto = cntx
        self.ponteiro = [0,0] # L,C
    
    def keyPress(self, key : chr):
        pass


    