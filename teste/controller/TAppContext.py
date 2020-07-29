import sys
import os
sys.path.append( os.path.abspath(".") )

from classes.controller.appcontext import AppContext
from classes.controller.contexto import Contexto
from classes.util.file import File

class TAppContext:

    def test_app_instantiate(self):
        try:
            app = AppContext()
        except Exception as e:
            assert False
        finally:
            assert True

    def test_app_open_arqv(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        arquivo = app.openArquivo(pathname,filename)
        assert len(arquivo.conteudo) == 4

    def test_app_open_cntx_no_config(self):
        os.remove("config.json")
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert contexto.ponteiro == [0,0]

    def test_app_open_cntx(self):
        app = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert len(contexto.arquivo.conteudo) == 4

    def test_app_open_cntx_includes(self):
        app = AppContext()
        arquivo = "exemplo/teste.c"
        pathname, filename = File.splitFilePath(arquivo) 
        contexto = app.open(pathname,filename)
        assert len(contexto.includes) > 0

    def test_app_save_pointer(self):
        app1 = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo) 
        try:
            contexto1 = app1.open(pathname,filename)
            app1.castWSSettingsW(contexto1.arquivo.local, [1,1])
        except Exception as e:
            assert False
        finally:
            assert True
    
    def test_app_load_pointer(self):
        app2 = AppContext()
        arquivo = "exemplo/conteudo.txt"
        pathname, filename = File.splitFilePath(arquivo)
        contexto2 = app2.open(pathname,filename)
        assert contexto2.ponteiro == [1,1]

    def test_app_final(self):
        app = AppContext()
        assert app.finalizar()

    # def test_contexto_get_ponteiro(self):
    #     app = AppContext()
    #     arquivo = "exemplo/conteudo.txt"
    #     pathname, filename = File.splitFilePath(arquivo) 
    #     contexto = app.open(pathname,filename)
    #     assert contexto.ponteiro[0] == 1 and contexto.ponteiro[1] == 1

    # def test_contexto_save(self):
    #     app = AppContext()
    #     arquivo = "exemplo/conteudo.txt"
    #     pathname, filename = File.splitFilePath(arquivo) 
    #     contexto = app.open(pathname,filename)
    #     # Salvar
    #     contexto.arquivo.conteudo = ["conteudo","1","2","3"]
    #     tamInicio = len(contexto.arquivo.conteudo)
    #     contexto.save()
    #     # Ler
    #     contexto.arquivo.conteudo=[]
    #     contexto.arquivo.ler()
    #     assert len(contexto.arquivo.conteudo) == tamInicio

    # def test_contexto_conteudo(self):
    #     app = AppContext()
    #     arquivo = "exemplo/conteudo.txt"
    #     pathname, filename = File.splitFilePath(arquivo) 
    #     contexto = app.open(pathname,filename)
    #     assert contexto.arquivo.conteudo == ["conteudo","1","2","3"]
