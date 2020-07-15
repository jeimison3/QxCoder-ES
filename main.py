import sys
from classes.controller.appcontext import AppContext
from classes.view.interface import Interface
from classes.model.arquivo import Arquivo
from classes.util.file import File

if __name__ == '__main__':
    arquivos = sys.argv[1:]

    if len(arquivos) == 0:
        arquivos = ["exemplo/teste.c"] # Temporário
        # arquivos = ["main.c"]

    app = AppContext() # Abrindo projeto
    for arq in arquivos:
        pathname, filename = File.splitFilePath(arq) 
        app.open(pathname,filename,True)
        

    for i in app.contextdelivery.contextos:
        print("Arquivo lido:",i.arquivo.local)
        for j in i.includes:
            print("|=>",j.local)
    interface = Interface(app.contextdelivery.contextos, app)

