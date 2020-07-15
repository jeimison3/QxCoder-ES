from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File

class TestContexto:
    def __init__(self):
        self.app = AppContext()
        self.testOpen()
        self.conteudo()
        self.testSave()

    def testOpen(self):
        print("> Teste open()")
        arquivos = ["exemplo/teste.c"]
        for arq in arquivos:
            pathname, filename = File.splitFilePath(arq) 
            self.contexto = self.app.open(pathname,filename,True)
        print("> Erros open(): ", self.app.arquivosErros )

    def conteudo(self):
        print("> Teste arquivo.conteudo")
        print("> ", self.contexto.arquivo.conteudo)

    def testSave(self):
        print("> Teste save()")
        self.contexto.save()
