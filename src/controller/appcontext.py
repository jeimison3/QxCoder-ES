from src.controller.filedelivery import FileDelivery
from src.controller.contextdelivery import ContextDelivery

class AppContext:
    '''
    Cria deliveries de cada serviço consumido.\n
    @param isNew : True para novo projeto, False para abrindo projeto\n
    @param projectPath : Local do projeto
    '''
    def __init__(self, isNew : bool, projectPath:str):
        self.isNew = isNew
        self.filedelivery = FileDelivery(projectPath)
        self.contextdelivery = ContextDelivery()

    def open(self, listFiles:list):
        '''
        Retorna List de Contexto de todos arquivos do projeto.\n
        @param List com nome de todos arquivos do projeto
        '''
        for arq in listFiles:
            self.openContexto(arq) # Abre Contexto para cada arquivo
        return self.contextdelivery.contextos

    def getWorkspaceSettings(self, filename):
        '''
        Le o arquivo de configuração e retorna a configuração para o arq em questão:
        @param Nome do arquivo\n
        @return Objeto de configuração do .json
        '''
        with open("config.json", "r") as arq:
            obj = json.load(arq)
        return obj[filename]


    def whiteWorkspaceSettings(self, filename, linha, coluna)
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
        with open('config.json', 'r') as arq:
            dados = json.load(arq) # Leio o arq .json
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
            

    def openArquivo(self, filename):
        '''
        @param Nome do arquivo\n
        @return Arquivo instanciado
        '''
        return self.filedelivery.open(filename)

    def openContexto(self, filename):
        '''
        Retorna contexto de arquivo e includes dele.\n
        @param Nome do arquivo\n
        @return Contexto instanciado
        '''
        arquivo = self.openArquivo(filename) # Pega Arquivo
        contexto = self.contextdelivery.open(arquivo) # Pega Contexto
        includeNames = contexto.listIncludes() # Pega list com local dos includes
        listaDosIncludesEmArquivos = []
        for includeName in includeNames:
            listaDosIncludesEmArquivos.append( self.openArquivo( includeName ) ) # Pega Arquivo para cada include encontrado
        contexto.includes = listaDosIncludesEmArquivos # Atribui list de Arquivo dos includes ao Contexto
        return contexto

    
