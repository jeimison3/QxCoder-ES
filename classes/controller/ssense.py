from classes.model.deepssense import DeepSSense,CodeCompletion,buscaTipo

class SSense: # Equivalente ao IntelliSense
    '''
    Mecanismo de sugestão de código
    @param Contexto
    '''

    def __init__(self, contexto):
        self.contexto = contexto # Irá analisar o conteudo dos arquivos
        self.dess = DeepSSense(contexto)

    def update(self,arquivo):
        self.dess.updateArquivo(arquivo)

    def getSugestao(self):
        '''
        Busca sugestões mais provaveis e retorna.\n
        @return [
            'complemento':'intf(',
            'sugestoes':[{
                'nome':'printf',
                'params':[('char *','str'),('...','args')]
            },
            ...
            ]
        ]\n
        { 'complemento' as String, 'sugestoes' as CodeCompletion[] }
        '''
        self.update(self.contexto.arquivo) # Notifica que código foi editado
        listaBuscaBinaria = self.dess.funcoes + self.dess.typedefs + self.dess.structs + self.dess.variaveis

        cLine = self.contexto.ponteiro[0]
        cColFinal = self.contexto.ponteiro[1]

        # if self.contexto.arquivo.conteudo[cLine][cColFinal-1] == '(':
        #     for char in reversed(range(cColFinal)):
        #         if self.contexto.arquivo.conteudo[cLine][char] != ' ':
        #             cColFinal = char
        #             break

        cColInicial = cColFinal
        for char in reversed(range(cColFinal)):
            if self.contexto.arquivo.conteudo[cLine][char] in [" ","\t"]:
                cColInicial = char+1
                break
            if char == 0:
                cColInicial = 0

        if cColFinal == cColInicial:
            return []
        
        wordSearch = self.contexto.arquivo.conteudo[cLine][cColInicial:cColFinal]
        # print("??["+wordSearch+"]")
        # for itm in listaBuscaBinaria:
        #     print("||=>"+itm.nome)
        lFim = buscaTipo(wordSearch, listaBuscaBinaria)
        
        return lFim



    