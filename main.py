import sys
from src.controller.appcontext import AppContext
from src.view.interface import Interface
from src.model.arquivo import Arquivo
from src.util.file import File

if __name__ == '__main__':
    arquivos = sys.argv[1:]
    arquivos = ["exemplo/teste.c"] # Temporário

    if len(arquivos) == 0:
        app = AppContext(True, File.userPath()) # Novo projeto
    else:
        app = AppContext(False, File.splitFilePath(arquivos[0])[0]) # Abrindo projeto

    print("Local do projeto: %s" % (app.filedelivery.projectPath))

    contextos = app.open(arquivos)
    interface = Interface(contextos)

