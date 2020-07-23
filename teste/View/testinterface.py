from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File
from classes.view.interface import Interface

class TestContexto:
    
    def __init__(self):
        
        self.app = AppContext()
        self.interface = Interface(self.app,breakFlag = True)

        self.conteudo = ["#define Teste_Interface True","","int main(){","\t return 0;","}"]

        self.arquivo1 = ["tmpFiles/teste1.c"]
        self.arquivo2 = ["tmpFiles/teste2.c"]


        self.testOpen()
        self.testWrite()
        self.testRead()

        #self.conteudo()
        #self.setPonteiro(1,1)
        #self.testSave()

    def testOpen(self):

        self.interface.open(self.arquivo1)
        self.interface.open(self.arquivo2)

        self.interface.janelas[0].contexto.arquivo.conteudo = conteudo
        self.interface.janelas[1].contexto.arquivo.conteudo = conteudo

    def testSetConteudo(self):

        self.interface.janelas[0].contexto.arquivo.conteudo = conteudo
        self.interface.janelas[1].contexto.arquivo.conteudo = conteudo
    
    def testWrite(self):

        for j in self.interface.janelas:

            j.writeRequest()

    def testRead():

        del self.app
        del self.interface

        self.app = AppContext()
        self.interface = Interface(self.app,breakFlag = True)

        self.interface.open(self.arquivo1)
        self.interface.open(self.arquivo2)

        assert self.interface.janelas[0].contexto.arquivo.conteudo == conteudo
        assert self.interface.janelas[1].contexto.arquivo.conteudo == conteudo





    #def testOpen(self):
    #    print("> Teste open()")
    #    arquivos = ["exemplo/teste.c"]
    #    for arq in arquivos:
    #        pathname, filename = File.splitFilePath(arq) 
    #        self.contexto = self.app.open(pathname,filename,True)
    #    print("> Erros open(): ", self.app.arquivosErros )

    #def setPonteiro(self,l,c):
    #    print("> Teste setPonteiro(%s,%s)" % (l,c))
    #    self.contexto.ponteiro = [l,c]

    #def getPonteiro(self):
    #   print("> Teste getPonteiro()")
    #    print("Ponteiro (L:%s, C:%s)" % (self.contexto.ponteiro[0],self.contexto.ponteiro[1]))

    #def conteudo(self):
    #    print("> Teste arquivo.conteudo")
    #    print("> ", self.contexto.arquivo.conteudo)

    #def testSave(self):
    #    print("> Teste save()")
    #    self.contexto.save()
