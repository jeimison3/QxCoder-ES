import sys
from src.controller.appcontext import AppContext
from src.view.interface import Interface
from src.model.arquivo import Arquivo
from src.util.file import File

if __name__ == '__main__':
    arquivos = sys.argv[1:]
    arquivos = ["exemplo/teste.c"] # Temporário

    if len(arquivos) == 0:
        app = AppContext(True) # Novo projeto
    else:
        app = AppContext(False) # Abrindo projeto
        for arq in arquivos:

            pathname, filename = File.splitFilePath(arq) 
            app.open(pathname,filename)

    print( app.arquivosErros )

    for i in app.contextdelivery.contextos:
        print("Arquivo lido:",i.arquivo.local)
        for j in i.includes:
            print("|=>",j.local)
    interface = Interface(app.contextdelivery.contextos, app)

