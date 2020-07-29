import sys
import os
sys.path.append( os.path.abspath(".") )

from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File

class TSSense:

    def test_ssense_open(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert len(contexto.arquivo.conteudo) > 0

    def test_ssense_open_update(self):
        app = AppContext()
        arquivo = "exemplo/teste.c"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ssense.update( contexto.includes[0] )
        assert True

    def test_ssense_vars(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert len(contexto.ssense.dess.variaveis) > 0
    
    def test_ssense_sugest_var(self):
        app = AppContext()
        arquivo = "exemplo/teste_var.h"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [2,5] # unsign
        retorno = contexto.ssense.getSugestao()
        assert retorno[0].nome == "unsigned"

    def test_ssense_sugest_varname(self):
        app = AppContext()
        arquivo = "exemplo/teste_var.h"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        
        contexto.ponteiro = [3,2] # var
        retorno1 = contexto.ssense.getSugestao()

        contexto.ponteiro = [4,4] # outra_var
        retorno2 = contexto.ssense.getSugestao()

        if len(retorno1) > 0 and len(retorno2) > 0:
            assert retorno1[0].nome == "var" and retorno2[0].nome == "outra"
        else: assert False

    def test_ssense_sugest_func(self):
        app = AppContext()
        arquivo = "exemplo/teste_func.h"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)

        contexto.ponteiro = [6,3] # noparam
        retorno1 = contexto.ssense.getSugestao()

        contexto.ponteiro = [7,3] # wparam
        retorno2 = contexto.ssense.getSugestao()

        for itm in retorno1+retorno2:
            print("=>",itm.nome, itm.params ,":"+itm.retorno)
        if len(retorno1) > 0 and len(retorno2) > 0:
            assert retorno1[0].nome == "noparam" and retorno2[0].nome == "wparam"
        else: assert False


    def test_ssense_sugest_struct(self):
        app = AppContext()
        arquivo = "exemplo/teste_struct.h"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [9,2] # te _teste
        retorno = contexto.ssense.getSugestao()
        for itm in retorno:
            print("=>",itm.nome,itm.params)
        if len(retorno) > 0:
            assert retorno[0].nome == "struct teste"
        else: assert False

    def test_ssense_sugest_typedef_struct(self):
        app = AppContext()
        arquivo = "exemplo/teste_struct.h"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [9,2] # te _teste
        retorno = contexto.ssense.getSugestao()
        for itm in retorno:
            print("=>",itm.nome,itm.params)
        if len(retorno) > 1:
            assert retorno[1].nome == "teste2"
        else: assert False

