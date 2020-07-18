from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File

class TestContexto:
    def __init__(self):
        self.app = AppContext()
        self.testOpen()
        self.getPonteiro()
        self.conteudo()
        self.setPonteiro(1,1)
        self.testSave()

    def testOpen(self):
        print("> Teste open()")
        arquivos = ["exemplo/teste.c"]
        for arq in arquivos:
            pathname, filename = File.splitFilePath(arq) 
            self.contexto = self.app.open(pathname,filename,True)
        print("> Erros open(): ", self.app.arquivosErros )

    def setPonteiro(self,l,c):
        print("> Teste setPonteiro(%s,%s)" % (l,c))
        self.contexto.ponteiro = [l,c]

    def getPonteiro(self):
        print("> Teste getPonteiro()")
        print("Ponteiro (L:%s, C:%s)" % (self.contexto.ponteiro[0],self.contexto.ponteiro[1]))

    def conteudo(self):
        print("> Teste arquivo.conteudo")
        print("> ", self.contexto.arquivo.conteudo)

    def testSave(self):
        print("> Teste save()")
        self.contexto.save()
