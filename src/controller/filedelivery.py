from src.model.arquivo import Arquivo

class FileDelivery:
    def __init__(self, projectPath):
        self.projectPath = projectPath
        self.files = []

    def open(self, filename):
        for arqv in self.files:
            if arqv.local == filename:
                return arqv
        novo = Arquivo(filename)
        self.files.append(novo)
        return novo