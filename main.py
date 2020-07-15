import sys
from src.controller.appcontext import AppContext
from src.view.interface import Interface
from src.model.arquivo import Arquivo
from src.util.file import File

if __name__ == '__main__':
    arquivos = sys.argv[1:]

    if len(arquivos) == 0:
        arquivos = ["exemplo/teste.c"] # Temporário

    app = AppContext() # Abrindo projeto
    for arq in arquivos:
        pathname, filename = File.splitFilePath(arq) 
        app.open(pathname,filename,True)
        

    print("ERR=", app.arquivosErros )

    for i in app.contextdelivery.contextos:
        print("Arquivo lido:",i.arquivo.local)
        for j in i.includes:
            print("|=>",j.local)
    interface = Interface(app.contextdelivery.contextos, app)

