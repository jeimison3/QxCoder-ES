from src.model.arquivo import Arquivo
from src.model.includes import Includes

class Contexto:
    def __init__(self, arquivo:Arquivo):
        self.arquivo = arquivo
        self.ponteiro = ()
        self.includes = []

    def getIncludesNames(self):
        return Includes.listar(self.arquivo)

    def addInclude(self, arqv : Arquivo):
        self.includes.append(arqv)
