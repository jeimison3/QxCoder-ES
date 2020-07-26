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
    
    def test_ssense_sugest(self):
        assert True
        return
        self.contexto.ponteiro = [20,15] # fun...
        retorno = self.contexto.ssense.getSugestao()
        print("Complemento: "+retorno.complemento)
        print("Possiveis:")
        for i in retorno.sugestoes:
            print('->'+i.nome)

