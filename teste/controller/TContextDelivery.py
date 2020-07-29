import sys
import os
sys.path.append( os.path.abspath(".") )

from classes.model.arquivo import Arquivo
from classes.controller.filedelivery import FileDelivery
from classes.controller.contextdelivery import ContextDelivery
from classes.util.file import File

class TContextDelivery:

    def test_contextdelivery_op_one(self):
        local = "exemplo/conteudo.txt"
        arq = Arquivo(local)
        cd = ContextDelivery(None)
        contx = cd.open(arq)
        assert len(contx.arquivo.conteudo) == 4

    def test_contextdelivery_multi_op_eq(self):
        local = "exemplo/conteudo.txt"
        arq = Arquivo(local)
        cd = ContextDelivery(None)
        contx1 = cd.open(arq)
        contx2 = cd.open(arq)
        assert contx1 == contx2

    def test_contextdelivery_multi_op_df(self):
        local1 = "exemplo/conteudo.txt"
        local2 = "exemplo/teste.c"
        arq1 = Arquivo(local1)
        arq2 = Arquivo(local2)
        cd = ContextDelivery(None)
        contx1 = cd.open(arq1)
        contx2 = cd.open(arq2)
        assert contx1 != contx2
