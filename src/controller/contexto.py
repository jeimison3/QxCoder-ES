from src.model.arquivo import Arquivo
from src.model.includes import Includes

class Contexto:
    def __init__(self, arquivo:Arquivo):
        self.arquivo = arquivo
        self.includes = []

    def listIncludes(self):
        return Includes.listar(self.arquivo)
