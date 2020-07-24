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

        interface.janelas[0].format.addChar('T')
        interface.janelas[0].format.addChar('e')
        interface.janelas[0].format.addChar('s')
        interface.janelas[0].format.addChar('t')
        interface.janelas[0].format.addChar('e')

        assert interface.janelas[0].contexto.arquivo.conteudo[0] == "Teste"


    def testRemove(self):

        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)

        arquivo = "teste.c"
        
        interface.open(arquivo)

        interface.janelas[0].format.addChar('T')
        interface.janelas[0].format.addChar('e')
        interface.janelas[0].format.addChar('s')
        interface.janelas[0].format.addChar('T')
        interface.janelas[0].format.addChar('e')

        interface.janelas[0].format.removeChar()
        interface.janelas[0].format.removeChar()
        interface.janelas[0].format.removeChar()
        
        assert interface.janelas[0].contexto.arquivo.conteudo[0] == "Te"

    
    def testLines(self):

        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)

        arquivo = "teste.c"
        
        interface.open(arquivo)

        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()

        
        assert len(interface.janelas[0].contexto.arquivo.conteudo) == 6

    def testPonteiro(self):

        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)

        arquivo = "teste.c"
        
        interface.open(arquivo)

        interface.janelas[0].format.addChar('T')
        interface.janelas[0].format.addChar('e')
        interface.janelas[0].format.addChar('s')
        interface.janelas[0].format.addChar('t')
        interface.janelas[0].format.addChar('e')

        assert interface.janelas[0].ponteiro[1] == 5

        interface.janelas[0].format.removeChar()
        interface.janelas[0].format.removeChar()
        interface.janelas[0].format.removeChar()

        assert interface.janelas[0].ponteiro[1] == 2

        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()
        interface.janelas[0].format.addLine()

        assert interface.janelas[0].ponteiro[0] == 5

        



