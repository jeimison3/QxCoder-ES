import sys
import os
sys.path.append( os.path.abspath(".") )

from classes.model.arquivo import Arquivo
from classes.util.file import File

class TArquivo:

    def test_arquivo_open(self):
        local = "exemplo/conteudo.txt"
        arq = Arquivo(local)
        assert len(arq.conteudo) == 4

    def test_arquivo_save(self):
        local = "exemplo/conteudo.txt"
        arq = Arquivo(local)
        arq.conteudo = ["conteudo","1","2","3"]
        tamInicio = len(arq.conteudo)
        arq.salvar()
        arq = Arquivo(local)
        assert len(arq.conteudo) == tamInicio
