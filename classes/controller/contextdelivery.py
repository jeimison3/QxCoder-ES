from classes.controller.contexto import Contexto

class ContextDelivery:
    def __init__(self, app):
        self.app = app
        self.contextos = []

    def open(self, arquivo):
        for cntx in self.contextos:
            if cntx.arquivo == arquivo:
                return cntx
        novo = Contexto(arquivo, self.app)
        self.contextos.append(novo)
        return novo