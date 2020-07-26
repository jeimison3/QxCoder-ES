import sys
import os
sys.path.append( os.path.abspath(".") )

from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File
from classes.view.interface import Interface

class TInterface:
    
    def testOpen(self):
        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)
        arquivo1 = "exemplo/teste1.c"
        arquivo2 = "exemplo/teste2.c"
        interface.open(arquivo1)
        interface.open(arquivo2)
        interface.janelas[0].contexto.arquivo.conteudo = "Teste"
        interface.janelas[1].contexto.arquivo.conteudo = "Teste"


    
    def testWrite(self):
        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)
        arquivo1 = "exemplo/teste1.c"
        arquivo2 = "exemplo/teste2.c"
        interface.open(arquivo1)
        interface.open(arquivo2)
        interface.janelas[0].contexto.arquivo.conteudo = "Teste"
        interface.janelas[1].contexto.arquivo.conteudo = "Teste"
        for j in interface.janelas:
            j.writeRequest()



    def testRead(self):
        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)        
        arquivo1 = "exemplo/teste1.c"
        arquivo2 = "exemplo/teste2.c"
        interface.open(arquivo1)
        interface.open(arquivo2)
        interface.janelas[0].contexto.arquivo.conteudo = "Teste"
        interface.janelas[1].contexto.arquivo.conteudo = "Teste"
        interface.janelas[0].writeRequest()
        interface.janelas[1].writeRequest()

        del app
        del interface

        app = AppContext()
        interface = Interface(app.contextdelivery.contextos, app,breakFlag = True)        
        arquivo1 = "exemplo/teste1.c"
        arquivo2 = "exemplo/teste2.c"
        interface.open(arquivo1)
        interface.open(arquivo2)
        assert interface.janelas[0].contexto.arquivo.conteudo == ['T','e','s','t','e']
        assert interface.janelas[1].contexto.arquivo.conteudo == ['T','e','s','t','e']





    #def testOpen(self):
    #    print("> Teste open()")
    #    arquivos = ["exemplo/teste.c"]
    #    for arq in arquivos:
    #        pathname, filename = File.splitFilePath(arq) 
    #        contexto = app.open(pathname,filename,True)
    #    print("> Erros open(): ", app.arquivosErros )

    #def setPonteiro(self,l,c):
    #    print("> Teste setPonteiro(%s,%s)" % (l,c))
    #    contexto.ponteiro = [l,c]

    #def getPonteiro(self):
    #   print("> Teste getPonteiro()")
    #    print("Ponteiro (L:%s, C:%s)" % (contexto.ponteiro[0],contexto.ponteiro[1]))

    #def conteudo(self):
    #    print("> Teste arquivo.conteudo")
    #    print("> ", contexto.arquivo.conteudo)

    #def testSave(self):
    #    print("> Teste save()")
    #    contexto.save()
