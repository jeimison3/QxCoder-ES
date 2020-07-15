from classes.controller.contexto import Contexto

class ContextDelivery:
    def __init__(self, app):
        self.app = app
        self.contextos = []

    def saveAll(self):
        for c in self.contextos:
            c.save()
    
    def savePointers(self):
        for c in self.contextos:
            c.savePointer()

    def open(self, arquivo):
        for cntx in self.contextos:
            if cntx.arquivo == arquivo:
                return cntx
        novo = Contexto(arquivo, self.app)
        self.contextos.append(novo)
        return novo