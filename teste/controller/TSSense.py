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

    def test_ssense_vars(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert len(contexto.ssense.dess.variaveis) > 0
    
    def test_ssense_sugest_var(self):
        app = AppContext()
        arquivo = "exemplo/teste.c"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [27,10] # unsign
        retorno = contexto.ssense.getSugestao()
        # for itm in retorno:
        #     print("=>",itm.nome)
        assert retorno[0].nome == "unsigned"

    def test_ssense_sugest_varname(self):
        app = AppContext()
        arquivo = "exemplo/teste.c"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [17,9] # teste
        retorno = contexto.ssense.getSugestao()
        # for itm in retorno:
        #     print("=>",itm.nome+"("+itm.retorno+")")
        if len(retorno) > 0:
            assert retorno[0].nome == "teste"
        else: assert False

    def test_ssense_sugest_func(self):
        app = AppContext()
        arquivo = "exemplo/teste.c"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [26,15] # fun
        retorno = contexto.ssense.getSugestao()
        # for itm in retorno:
        #     print("=>",itm.nome+"("+itm.retorno+")")
        if len(retorno) > 0:
            assert retorno[0].nome == "funcao"
        else: assert False


    def test_ssense_sugest_struct(self):
        app = AppContext()
        arquivo = "exemplo/teste.c"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [34,8] # Vecto
        retorno = contexto.ssense.getSugestao()
        # for itm in retorno:
        #     print("=>",itm.nome+"("+itm.retorno+")")
        if len(retorno) > 0:
            assert retorno[0].nome == "VetorNome"
        else: assert False

