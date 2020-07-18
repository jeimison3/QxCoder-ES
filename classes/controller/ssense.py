from classes.model.deepssense import DeepSSense,CodeCompletion

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

    def getSugestao(self,trecho='APAGAR ESTE PARÂMETRO'):
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
        self.dess.updateArquivo(self.contexto.arquivo) # Notifica que código foi editado
        
        listaBuscaBinaria = self.dess.funcoes + self.dess.typedefs + self.dess.structs + self.dess.variaveis
        
        # Implementa a busca binária e retorna a lista

        
        # Organiza as sugestões num array, 0: mais possível, 1: segundo mais possível...

        # Retorna na forma da estrutura 
        return [
            {
                'complemento':'rintf(',
                'params':'char*, ...'
            }
        ]
