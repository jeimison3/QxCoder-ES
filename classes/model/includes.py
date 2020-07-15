from classes.model.cprocessor import CProcessor
from classes.model.arquivo import Arquivo


class Includes:

    @staticmethod
    def listar(arquivo : Arquivo):
        print('procurando em:',arquivo.local)
        '''
        Método que retorna lista de nomes de arquivos referenciados no arquivo de entrada.\n
        @param Arquivo\n
        @return List de nomes de arquivos para incluir
        '''
        lista = []
        for linha in arquivo.conteudo:
            if str(linha).find('#include') >= 0:
                ret = CProcessor.getConteudoEntre(str(linha),"\"")
                if ret != None:
                    print('inc:',ret)
                    lista.append(ret)
        return lista 