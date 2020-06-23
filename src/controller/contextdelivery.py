from src.controller.contexto import Contexto

class ContextDelivery:
    def __init__(self):
        self.contextos = []


    def open(self, arquivo):
        for cntx in self.contextos:
            if cntx.arquivo == arquivo:
                return cntx
        novo = Contexto(arquivo)
        self.contextos.append(novo)
        return novo