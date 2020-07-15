from classes.util.file import File

class Arquivo:
    '''
    Classe para manipular um unico aquivo
    @param Local do arquivo
    '''

    def __init__(self,local,novo:bool=False):
        self.local = local
        self.conteudo = []
        if not novo:
            self.ler()

    def setConteudo(self, valor):
        '''
        Atribui conteúdo do arquivo
        '''
        self.conteudo = valor

    def getConteudo(self):
        '''
        Retorna conteúdo do arquivo\n
        @return Conteúdo
        '''
        return self.conteudo

    def ler(self):
        '''
        Lê e retorna conteúdo do arquivo\n
        @return Conteúdo
        '''
        with open(self.local, 'r', encoding = 'utf-8') as arq_entrada:
            for coisa in arq_entrada:
                temp = coisa.rstrip("\n")
                self.conteudo.append(temp)
            arq_entrada.close()
        
        return self.conteudo

        
    def salvar(self):
        '''
        Salva conteúdo do arquivo.
        '''
        nova = []
        for item in self.conteudo:
            nova.append(item + "\n")
        with open(self.local, 'w', encoding = 'utf-8') as arq_escrita:
            for item in nova:
                arq_escrita.write(item)
            arq_escrita.close()
        pass