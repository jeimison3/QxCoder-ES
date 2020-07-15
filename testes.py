import sys
from classes.controller.appcontext import AppContext
from classes.view.interface import Interface
from classes.model.arquivo import Arquivo
from classes.util.file import File

from teste.controller.testappcontext import TestAppContext

if __name__ == '__main__':
    testes = sys.argv[1:]

    if len(testes) == 0:
        print("Escolha o teste! ex.: TestAppContext")
        exit(0)

    
    if "TestAppContext" in testes:
        _test = TestAppContext()
        

