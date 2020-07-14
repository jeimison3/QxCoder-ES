class Arquivo:
    '''
    Classe para manipular um unico aquivo
    @param Local do arquivo
    '''

    def __init__(self,local):
        self.local = local
        self.conteudo = []
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
        
        return self.conteudo

        
    def salvar(self):
        '''
        Salva conteúdo do arquivo.
        '''
        nova = []
        for item in self.conteudo:
            nova.append(item + "\n")
        with open(self.local, 'w', encoding = 'utf-8') as arq_entrada:
            for item in nova:
                arq.write(item)
        pass