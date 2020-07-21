import json
from classes.controller.filedelivery import FileDelivery
from classes.controller.contextdelivery import ContextDelivery
from classes.util.file import File

class AppContext:
    '''
    Cria deliveries de cada serviço consumido.\n
    '''
    def __init__(self):
        self.arquivosErros = []
        self.filedelivery = FileDelivery()
        self.contextdelivery = ContextDelivery(self)

    def finalizar(self):
        # self.contextdelivery.savePointers()
        print('Finalizado.')

    def open(self, pathcall:str, arquivo:str, canCreate : bool = False):
        '''
        Retorna Contexto do arquivo.\n
        @param Nome do arquivo
        '''
        return self.openContexto(pathcall, arquivo, canCreate)

    def getWorkspaceSettings(self, filename):
        '''
        Le o arquivo de configuração e retorna a configuração para o arq em questão:
        @param Nome do arquivo\n
        @return Objeto de configuração do .json
        '''
        if not File.arquivoExiste("config.json"):
            return None

        with open("config.json", "r") as arq:
            obj = json.load(arq)
            if filename in obj:
                return obj[filename]
        return None


    def writeWorkspaceSettings(self, filename, linha, coluna):
        '''
        Escreve no arquivo .json as configurações do arquivo em questão\n
        @param Nome do arquivo, linha e coluna do cursor\n
        '''
        '''
        ARQUIVO ANTES: {}
        ARQUIVO DEPOIS:{
            "nome_do_arq":{
                "linha":"posição_da_linha"
                "coluna":"posição_da_coluna"
            }
        }
        '''
        # if not(os.path.exists('config.json')):
        #     with open('config.json', 'w') as arq:
        #         arq.write('{}')

        if File.arquivoExiste("config.json"):
            with open('config.json', 'r') as arq:
                dados = json.load(arq) # Leio o arq .json
        else:
            dados = {}

        dados_json = json.dumps(dados) # Transfromo em uma string

        if dados_json == '{}': # Testo pra ver se está vazio ou não
            # Se estiver, escrevo por cima a configuração do arq
            teste = {filename:{"linha":linha,"coluna":coluna}} 
            with open('config.json', 'w') as arq:
                json.dump(teste, arq, indent=4)
        else:
            # Se não, coloco o arquivo como um obj 
            with open("config.json", "r") as arq:
                obj = json.load(arq)
            # Acrescento a nova configuração no obj
            obj[filename] = {'linha':linha,'coluna':coluna}
            # Reescrevo no arquivo o obj atualizado
            with open("config.json", "w") as arq:
                json.dump(obj, arq, indent = 4)


    def castWSSettingsW(self,local,ponteiro):
        self.writeWorkspaceSettings(local, ponteiro[0], ponteiro[1])

    def castWSSettingsR(self,local):
        ponto = [0,0]
        sett = self.getWorkspaceSettings(local)
        if sett != None:
            if 'linha' in sett:
                ponto[0] = sett['linha']
            if 'coluna' in sett:
                ponto[1] = sett['coluna']
        return ponto
            

    def openArquivo(self, path, filename, canCreate : bool = False):
        '''
        @param Nome do arquivo\n
        @return Arquivo instanciado
        '''
        return self.filedelivery.open(path,filename,canCreate)

    def openContexto(self, pathCall, filename, canCreate : bool = False):
        '''
        Retorna contexto de arquivo e includes dele.\n
        @param Nome do arquivo\n
        @return Contexto instanciado
        '''
        arquivo = self.openArquivo(pathCall,filename,canCreate) # Pega Arquivo
        if arquivo == None:
            self.arquivosErros.append( (filename, "Erro ao abrir arquivo: não encontrado.") )
            return
        contexto = self.contextdelivery.open(arquivo) # Pega Contexto
        includeNames = contexto.getIncludesNames() # Pega list com local dos includes
        
        for includeName in includeNames:
            arqv = self.openArquivo( arquivo.local, includeName )
            if arqv == None:
                self.arquivosErros.append( (includeName, "Erro ao incluir arquivo: não encontrado.") )
            else:
                contexto.addInclude( arqv ) # Pega Arquivo para cada include encontrado
        
        return contexto

    def saveAll(self):
        self.contextdelivery.saveAll()
    
