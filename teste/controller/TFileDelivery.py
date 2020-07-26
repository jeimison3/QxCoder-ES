import sys
import os
sys.path.append( os.path.abspath(".") )

from classes.model.arquivo import Arquivo
from classes.controller.filedelivery import FileDelivery
from classes.util.file import File

class TFileDelivery:

    def test_filedelivery_open_one(self):
        fd = FileDelivery()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        arq = fd.open(pathname,filename)
        assert len(fd.files)

    def test_filedelivery_multi_op_eq(self):
        fd = FileDelivery()
        arquivo = "exemplo/conteudo.txt"
        pathname1, filename1 = File.splitFilePath(arquivo)
        pathname2, filename2 = File.splitFilePath(arquivo)
        arq1 = fd.open(pathname1,filename1)
        arq2 = fd.open(pathname2,filename2)
        assert arq1 == arq2

    def test_filedelivery_multi_op_df(self):
        fd = FileDelivery()
        arquivo1 = "exemplo/conteudo.txt"
        arquivo2 = "exemplo/teste.c"
        pathname1, filename1 = File.splitFilePath(arquivo1)
        pathname2, filename2 = File.splitFilePath(arquivo2)
        arq1 = fd.open(pathname1,filename1)
        arq2 = fd.open(pathname2,filename2)
        assert arq1 != arq2
