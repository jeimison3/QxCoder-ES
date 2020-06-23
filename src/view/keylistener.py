from enum import Enum

class Keys(Enum):
    KEY_ATALHO_NONE = 0,
    KEY_ATALHO_SALVAR = 1


class KeyListener:
    '''
    Classe com funções para reconhecimento de atalhos de teclado e interface geral entre teclas e janelas.
    '''
    def __init__(self, interface):
        self.interface = interface
        pass

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

