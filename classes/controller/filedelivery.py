from classes.model.arquivo import Arquivo
from classes.util.file import File

class FileDelivery:
    def __init__(self):
        self.files = []

    def open(self, who, where, canCreate : bool = False):
        for arqv in self.files:
            absWhere = File.getAbsPath(who,where)
            print("$ FileDelivery OPEN [%s] @ %s" % (where,absWhere))
            if absWhere == arqv.local:
                return arqv
        absNewWhere = File.getAbsPath(who,where)
        
        if File.arquivoExiste(absNewWhere):
            novo = Arquivo(absNewWhere)
            self.files.append(novo)
            return novo

        elif canCreate:
            novo = Arquivo(absNewWhere, True)
            self.files.append(novo)
            return novo

        else:
            return None