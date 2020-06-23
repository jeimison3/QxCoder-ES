class Arquivo:
    '''
    @param Local do arquivo
    '''

    def __init__(self,local):
        self.local = local
        self.conteudo = ""

    def setConteudo(self, valor):
        '''
        Atribui conteúdo do arquivo
        '''
        self.conteudo = valor

    def getConteudo(self, valor):
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
        #...
        self.conteudo = ""
        return self.conteudo

        
    def salvar(self):
        '''
        Salva conteúdo do arquivo.
        '''
        pass