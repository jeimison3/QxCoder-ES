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
                CodeCompletion('.',i+' *', '*') # Ponteiro
            )

        self.analisar()

    def analisar(self):
        for i in self.contexto.includes:
            self.updateArquivo(i)
        self.updateArquivo(self.contexto.arquivo)

    def updateArquivo(self, arquivo:Arquivo):
        for i in reversed(self.variaveis):
            if i.local == arquivo.local:
                self.variaveis.remove(i)
        for i in reversed(self.structs):
            if i.local == arquivo.local:
                self.structs.remove(i)
        for i in reversed(self.funcoes):
            if i.local == arquivo.local:
                self.funcoes.remove(i)
        for i in reversed(self.typedefs):
            if i.local == arquivo.local:
                self.typedefs.remove(i)
        self.buscaEm(arquivo)


    def buscaEm(self, arquivo:Arquivo):
        '''
        Itera conteúdo buscando definições.\n
        '''
        # print("Scan @ "+arquivo.local)
        padronizado = CProcessor.padronizaArquivo(arquivo.conteudo)
        listaTipos = self.funcoes + self.typedefs + self.structs + self.variaveis


        arqv = " ".join(padronizado)
        splt = arqv.split(" ")

        while("" in splt) : splt.remove("") 
        ids = []
        for i in range(len(splt)):
            if splt[i] == "#include":
                ids.append(i)
                ids.append(i+1)
        for i in reversed(ids):
            del(splt[i])

        # print(splt)
        i = len(splt)
        while i > 0:
            i = i -1

            if splt[i] == "}":
                aberto = 1
                j = i
                while aberto != 0 and j > 0:
                    j=j-1
                    if splt[j] == "}": aberto = aberto+1
                    if splt[j] == "{": aberto = aberto-1
                j = j-1
                if splt[j] == ")": # É função
                    fimParams = j
                    aberto = 1
                    while aberto != 0 and j > 0:
                        j=j-1
                        if splt[j] == ")": aberto = aberto+1
                        if splt[j] == "(": aberto = aberto-1
                    params = splt[j+1:fimParams]
                    params = " ".join(params)
                    params = params.split(",")
                    j = j-1
                    nome = splt[j]
                    iLastTipo = j-1
                    while True:
                        if not splt[iLastTipo-1] in [";", ",", "}" ,"\"",">"]:
                            iLastTipo = iLastTipo -1
                        else: break
                    tipo = " ".join(splt[iLastTipo:j]).strip()
                    j = iLastTipo-1
                    lista = buscaTipo( tipo , listaTipos)
                    if len(lista) > 0:
                        # print("NOME="+nome +" | TIPO="+tipo +" | PARAMS=",params)
                        cc = CodeCompletionMethod(arquivo.local, nome, 'METHOD', [])
                        cc.params = params
                        cc.retorno = lista[0].nome
                        self.funcoes.append(cc)

                else: # É struct
                    nome = splt[j]
                    parametros = splt[j+2:i]
                    iLastTipo = j-1
                    while True:
                        if not splt[iLastTipo-1] in [";", ",", "}" ,"\"",">"]:
                            iLastTipo = iLastTipo -1
                        else: break
                    i = j # Ignorar parâmetros dentro do struct
                    if " ".join(splt[iLastTipo:j]).strip() in ["struct","typedef struct",]:
                        tipo = "struct"
                        j = iLastTipo-1
                        
                        params = " ".join(parametros)
                        params = params.split(";")
                        for p in range(len(params)):
                            params[p] = params[p].strip()
                        while "" in params: params.remove("")

                        # print("NOME="+nome +" | TIPO="+tipo +" | PARAMS=",params )

                        cc = CodeCompletionStruct(arquivo.local, nome, 'STRUCT0', [])
                        cc.params = params
                        cc.retorno = nome
                        self.funcoes.append(cc)


            if splt[i] == "=" or (i > 0 and splt[i] == ";" and splt[i-1] != ")"):
                j = i-1
                isVetor = False
                isTypedef = False
                if splt[j] == "]":
                    while splt[j] != "[": j = j -1
                    isVetor = True
                    j = j-1
                nome = splt[j]
                # print("NOME?"+nome)
                iLastTipo = j-1
                while True:
                    if not splt[iLastTipo-1] in [";", ",", "{","}" ,"\"",">"]:
                        iLastTipo = iLastTipo -1
                    else: break

                if splt[iLastTipo] == "typedef":
                    isTypedef = True
                    iLastTipo= iLastTipo+1

                tipo = " ".join(splt[iLastTipo:j]).strip() + (" *" if isVetor else "")
                j = iLastTipo-1
                lista = buscaTipo( tipo , listaTipos)
                if len(lista) > 0:
                    # print("NOME="+nome +" | TIPO="+tipo)
                    cc = CodeCompletion(arquivo.local, nome, 'VAR')
                    cc.retorno = lista[0].nome
                    if isTypedef:
                        self.typedefs.append(cc)
                    else:
                        self.variaveis.append(cc)


            else:
                continue



def buscaTipo(busca,lista):
    '''
    unsig, [...]
    '''
    escolhidos = []
    for itm in lista:
        if itm.nome.find( busca )>-1 and (not itm in escolhidos):
            escolhidos.append(itm)
    escolhidos.sort(key=lambda x: x.nome)
    return escolhidos


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
    