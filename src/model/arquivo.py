class Arquivo:
    '''
    Classe para manipular um unico aquivo
    @param Local do arquivo
    '''

    def __init__(self,local):
        self.local = local
        self.conteudo = []

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
        with open(self.local, 'r', encoding= 'utf-8') as arq_entrada:
            for coisa in arq_entrada:
                self.conteudo.append(coisa)
        
        return self.conteudo

        
    def salvar(self):
        '''
        Salva conteúdo do arquivo.
        '''
        pass