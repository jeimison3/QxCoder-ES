from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File

class TestSSense:
    def __init__(self):
        self.app = AppContext()
        self.testOpen()
        self.printPadronizados()
        self.estruturas()
        #self.ssense() # Incompleto

    def testOpen(self):
        print("> Teste open()")
        arquivos = ["exemplo/teste.c"]
        for arq in arquivos:
            pathname, filename = File.splitFilePath(arq) 
            self.contexto = self.app.open(pathname,filename,True)
        print("> Erros open(): ", self.app.arquivosErros )

    def printPadronizados(self):
        self.contexto.ssense.dess.printPadronizados()

    def ssense(self):
        self.contexto.ponteiro = [20,15] # fun...
        retorno = self.contexto.ssense.getSugestao()
        print("Complemento: "+retorno.complemento)
        print("Possiveis:")
        for i in retorno.sugestoes:
            print('->'+i.nome)

    def estruturas(self):
        print("> Listar estruturas")
        print("#--> Variáveis")
        for i in self.contexto.ssense.dess.variaveis:
            print("|--> ", i.nome)
        print("#--> Structs")
        for i in self.contexto.ssense.dess.structs:
            print("|--> ", i.nome)
        print("#--> Typedefs")
        for i in self.contexto.ssense.dess.typedefs:
            print("|--> ", i.nome)
        print("#--> Funções")
        for i in self.contexto.ssense.dess.funcoes:
            print("|--> ", i.nome)
