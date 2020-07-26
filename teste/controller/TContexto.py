import sys
import os
sys.path.append( os.path.abspath(".") )

from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File

class TContexto:

    def test_contexto_open(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert len(contexto.arquivo.conteudo) == 4

    def test_contexto_set_ponteiro(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        contexto.ponteiro = [1,1]
        contexto.save()
        assert contexto.ponteiro[0] == 1 and contexto.ponteiro[1] == 1

    def test_contexto_get_ponteiro(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert contexto.ponteiro[0] == 1 and contexto.ponteiro[1] == 1

    def test_contexto_save(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        # Salvar
        contexto.arquivo.conteudo = ["conteudo","1","2","3"]
        tamInicio = len(contexto.arquivo.conteudo)
        contexto.save()
        # Ler
        contexto.arquivo.conteudo=[]
        contexto.arquivo.ler()
        assert len(contexto.arquivo.conteudo) == tamInicio

    def test_contexto_conteudo(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert contexto.arquivo.conteudo == ["conteudo","1","2","3"]
