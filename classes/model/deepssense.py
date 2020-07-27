from classes.model.arquivo import Arquivo
from classes.model.cprocessor import CProcessor

class DeepSSense:
    def __init__(self,cntx):
        self.contexto = cntx
        # 1. Busca variáveis
        self.variaveis = []
        # 2. Busca structs
        self.structs = []
        # 3. Busca typedefs (considera os anteriores)
        self.typedefs = []
        # 4. Busca funções (usa os anteriores)
        self.funcoes = []
        
        variaveisBasicas = ["void", "char", "signed char", "unsigned char", "short" ,"short int", "signed short", "signed short int", "unsigned short", "unsigned short int", "int", "signed", "signed int", "unsigned", "unsigned int", "long" , "long int", "signed long", "signed long int", "unsigned long", "unsigned long int", "long long", "long long int", "signed long long", "signed long long int", "unsigned long long", "unsigned long long int", "float", "double", "long double"]
        # https://en.wikipedia.org/wiki/C_data_types

        for i in variaveisBasicas:
            self.variaveis.append(
                CodeCompletion('.',i, '')
            )
            # A função padronizaArquivo vai garantir a estrutura abaixo:
            self.variaveis.append(
                CodeCompletion('.',i+' *', '') # Ponteiro
            )
        self.analisar()

    def analisar(self):
        self.updateArquivo(self.contexto.arquivo)
        for i in self.contexto.includes:
            self.updateArquivo(i)

    def updateArquivo(self, arquivo:Arquivo):
        for i in self.variaveis:
            if i.local == arquivo.local:
                self.variaveis.remove(i)
        for i in self.structs:
            if i.local == arquivo.local:
                self.structs.remove(i)
        for i in self.typedefs:
            if i.local == arquivo.local:
                self.typedefs.remove(i)
        self.buscaEm(arquivo)


    def buscaEm(self, arquivo:Arquivo):
        '''
        Itera conteúdo buscando definições.\n
        '''
        padronizado = CProcessor.padronizaArquivo(arquivo.conteudo)

        # print("#############")
        # for i in padronizado:
        #     print(i)
        # print("#############")

        
    


class CodeCompletion:
    local = "" # Arquivo em que foi definido 
    nome = "" # Nome da estrutura
    retorno = "" # Tipo de retorno
    tipo = "VAR" # String da classe
    def __init__(self, local, nome, tipo):
        self.local = local
        self.nome = nome
        self.tipo = tipo

class CodeCompletionStruct(CodeCompletion):
    tipo = "STRUCT"
    params = [] # [ ('int *','ponteiroNumero'), ... ]
    def __init__(self, local, nome, tipo, params = []):
        super().__init__(local, nome, tipo)

class CodeCompletionMethod(CodeCompletion):
    tipo = "METHOD"
    params = [] # [ ('int *','ponteiroNumero'), ... ]
    def __init__(self, local, nome, tipo, params = []):
        super().__init__(local, nome, tipo)
    