import sys
from classes.controller.appcontext import AppContext
from classes.view.interface import Interface
from classes.model.arquivo import Arquivo
from classes.util.file import File
import signal
import curses

if __name__ == '__main__':
    arquivos = sys.argv[1:]

    if len(arquivos) == 0:
        arquivos = ["exemplo/teste.c"] # Temporário
        # arquivos = ["main.c"]

    try:
        app = AppContext() # Abrindo projeto
        for arq in arquivos:
            pathname, filename = File.splitFilePath(arq) 
            app.open(pathname,filename,True)
    except Exception as e:
        print('Erro no processamento do contexto.')
        raise e


    # Tratamento de fechamento
    def signal_handler(sig, frame):
        curses.endwin()
        app.finalizar()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
        
    
    for i in app.contextdelivery.contextos:
        print("Arquivo lido:",i.arquivo.local)
        for j in i.includes:
            print("|=>",j.local)
    
    try:
        interface = Interface(app.contextdelivery.contextos, app)
    except Exception as e:
        curses.endwin()
        print('Erro na interface:')
        raise e
        sys.exit(0)

