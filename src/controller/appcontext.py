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

    def getWorkspaceSettings(self):
        # E aí?
        pass

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

    
