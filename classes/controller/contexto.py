from classes.model.arquivo import Arquivo
from classes.model.includes import Includes

class Contexto:
    def __init__(self, arquivo:Arquivo, app):
        self.arquivo = arquivo
        self.app = app # AppContext
        self.ponteiro = app.castWSSettingsR(arquivo)

        if self.ponteiro[0]+1 > len(self.arquivo.conteudo):
            self.ponteiro[0] = len(self.arquivo.conteudo)-1
        if self.ponteiro[1]+1 > len(self.arquivo.conteudo[self.ponteiro[0]]):
            self.ponteiro[1] = len(self.arquivo.conteudo[self.ponteiro[0]])-1
        self.includes = []

    def getIncludesNames(self):
        return Includes.listar(self.arquivo)

    def addInclude(self, arqv : Arquivo):
        self.includes.append(arqv)

    def savePointer(self):
        self.app.castWSSettingsW(self.arquivo.local, self.ponteiro)

    def save(self):
        self.arquivo.salvar()
        self.savePointer()
