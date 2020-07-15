from classes.controller.appcontext import AppContext
from classes.util.file import File

class TestAppContext:
    def __init__(self):
        self.app = AppContext()
        self.testOpen()
        self.testSaveAll()

    def testOpen(self):
        print("> Teste open()")
        arquivos = ["exemplo/teste.c"]
        for arq in arquivos:
            pathname, filename = File.splitFilePath(arq) 
            self.app.open(pathname,filename,True)
        
        print("> Erros open(): ", self.app.arquivosErros )

    def testSaveAll(self):
        print("> Teste saveAll()")
        self.app.saveAll()
