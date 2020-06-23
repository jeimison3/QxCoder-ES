from src.controller.contexto import Contexto

class SSense: # Equivalente ao IntelliSense
    '''
    Mecanismo de sugestão de código
    @param Contexto
    '''

    def __init__(self, contexto : Contexto):
        self.contexto = contexto # Irá analisar o conteudo dos arquivos

    def deepAnalise(self, trecho):
        # Percorre cada arquivo do contexto
        return ["...","...","..."]

    def getSugestao(self, trecho):
        '''
        Sugere complemento do código com base no contexto.\n
        @param Linha do código a ser completada
        '''

        possiveisSugestoes = self.deepAnalise(trecho)

        # Organiza as sugestões num array, 0: mais possível, 1: segundo mais possível...

        # Retorna
        return [
            {
                'complemento':'rintf(',
                'params':'char*, ...'
            }
        ]
