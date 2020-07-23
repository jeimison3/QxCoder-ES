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

    def setPonteiro(self,l,c):
        print("> Teste setPonteiro(%s,%s)" % (l,c))
        self.contexto.ponteiro = [l,c]

    def getPonteiro(self):
        print("> Teste getPonteiro()")
        print("Ponteiro (L:%s, C:%s)" % (self.contexto.ponteiro[0],self.contexto.ponteiro[1]))

    def conteudo(self):
        print("> Teste arquivo.conteudo")
        print("> ", self.contexto.arquivo.conteudo)

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
