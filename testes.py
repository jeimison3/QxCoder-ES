#!/usr/bin/env python3
import sys
from classes.controller.appcontext import AppContext
from classes.view.interface import Interface
from classes.model.arquivo import Arquivo
from classes.util.file import File

from teste.controller.testappcontext import TestAppContext
from teste.controller.testcontexto import TestContexto
from teste.controller.testssense import TestSSense

if __name__ == '__main__':
    testes = sys.argv[1:]

    if len(testes) == 0:
        testes = ["TestAppContext","TestContexto","TestSSense"]
        #print("Escolha o teste! ex.: TestAppContext, TestContexto, TestSSense")
        #exit(0)

    
    if "TestAppContext" in testes:
        _test = TestAppContext()
    if "TestContexto" in testes:
        _test = TestContexto()
    if "TestSSense" in testes:
        _test = TestSSense()
        

