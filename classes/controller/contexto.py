from classes.model.arquivo import Arquivo
from classes.model.includes import Includes

class Contexto:
    def __init__(self, arquivo:Arquivo, app):
        self.arquivo = arquivo
        self.app = app # AppContext
        self.ponteiro = app.castWSSettingsR(arquivo)
        self.includes = []

    def getIncludesNames(self):
        return Includes.listar(self.arquivo)

    def addInclude(self, arqv : Arquivo):
        self.includes.append(arqv)

    def save(self):
        self.arquivo.salvar()
        self.app.castWSSettingsW(self.arquivo.local, self.ponteiro)
