from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File
from classes.view.interface import Interface

class TJanela:

    def testAdd(self):

        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)
        arquivo = "teste.c"
        
        interface.open(arquivo)

        Interface.janelas[0].format.addChar('T')
        Interface.janelas[0].format.addChar('e')
        Interface.janelas[0].format.addChar('s')
        Interface.janelas[0].format.addChar('T')
        Interface.janelas[0].format.addChar('e')

        assert interface.janelas[0].contexto.arquivo.conteudo[0] == list("Teste")


    def testRemove(self):

        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)

        arquivo = "teste.c"
        
        interface.open(arquivo)

        Interface.janelas[0].format.addChar('T')
        Interface.janelas[0].format.addChar('e')
        Interface.janelas[0].format.addChar('s')
        Interface.janelas[0].format.addChar('T')
        Interface.janelas[0].format.addChar('e')

        Interface.janelas[0].format.removeChar()
        Interface.janelas[0].format.removeChar()
        Interface.janelas[0].format.removeChar()
        
        assert interface.janelas[0].contexto.arquivo.conteudo[0] == list("Te")

    
    def testLines(self):

        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)

        arquivo = "teste.c"
        
        interface.open(arquivo)

        Interface.janelas[0].format.addLine()
        Interface.janelas[0].format.addLine()
        Interface.janelas[0].format.addLine()
        Interface.janelas[0].format.addLine()
        Interface.janelas[0].format.addLine()

        
        assert len(interface.janelas[0].contexto.arquivo.conteudo) == 6

