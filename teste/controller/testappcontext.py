from classes.controller.appcontext import AppContext
from classes.util.file import File

class TestAppContext:
    def __init__(self):
        self.app = AppContext()
        print("> Teste open()")
        self.testOpen()

    def testOpen(self):
        arquivos = ["exemplo/teste.c"]
        for arq in arquivos:
            pathname, filename = File.splitFilePath(arq) 
            self.app.open(pathname,filename,True)
        
        print("> Erros open(): ", self.app.arquivosErros )
