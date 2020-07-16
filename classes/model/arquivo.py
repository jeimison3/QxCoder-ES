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
        temp = []
        with open(self.local, 'r', encoding = 'utf-8') as arq_entrada:
            temp = arq_entrada.readlines()
            arq_entrada.close()

        if "\n" in temp[len(temp) - 1]:
            temp.append('')

        for item in temp:
            self.conteudo.append(item.rstrip("\n"))
        
        
        return self.conteudo

        
    def salvar(self):
        '''
        Salva conteúdo do arquivo.
        '''
        with open(self.local, 'w', encoding = 'utf-8') as arq_escrita:
            arq_escrita.write("\n".join(self.conteudo))
            arq_escrita.close()
        pass