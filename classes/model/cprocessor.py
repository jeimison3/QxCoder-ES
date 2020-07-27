class CProcessor:
    @staticmethod
    def getConteudoEntre(tx : str, c:str, c2:str=''):
        if c2 == '':
            c2 = c
        conteudo = tx.split(c,1)
        if len(conteudo) >= 2:
            tmp = conteudo[1].split(c2,1)
            conteudo.remove(conteudo[1])
            conteudo = conteudo+tmp

        if len(conteudo) == 3:
            return conteudo[1]
        else:
            return None

    @staticmethod
    def getDefinicao(tx : str, sel:str, terms:list=["{","[","=",";",",",")"]):
        conteudo = tx.split(sel,1)
        if len(conteudo) == 2:
            for ter in terms:
                if ter in conteudo[1]:
                    tmp = conteudo[1].split(ter,1)
                    conteudo.remove(conteudo[1])
                    conteudo = conteudo+tmp
                if len(conteudo) == 3:
                    return conteudo[1]

        return None

    @staticmethod
    def contemTipo(tipo : str, linha : str):
        aceitaveisPre = [" ","(",")",","]
        aceitaveisPost = [" ","(",")","*"]
        if tipo in linha:
            inic = linha.find(tipo)
            fim = inic+len(tipo)
            if (inic > 0 and not linha[inic-1] in aceitaveisPre) or (fim+1<len(linha) and not linha[fim] in aceitaveisPost):
                return False
            return True
        return False


    @staticmethod
    def padronizaArquivo(conte : list):
        strings = []

        # Camuflar strings temporariamente
        tmpConteudo = "\n".join(conte).split("\"")
        for i in range(len(tmpConteudo)):
            if i%2 == 1:
                strings.append( tmpConteudo[i] )
                newI = len(strings)-1
                tmpConteudo[i]='$$$$$$$$$$$$'
        tmpConteudo = '\"'.join(tmpConteudo).split('\n')


        ret = []
        comentarioAberto = False
        for i in tmpConteudo:
            if len(i) > 0: # Tem conteúdo
                i = i.split('//')[0] # Elimina comentário
                while True:
                    eliminarComeco = len(i)-1 if len(i) > 0 else 0
                    eliminarFim = eliminarComeco

                    if comentarioAberto: # Se já definido
                        eliminarFim = eliminarComeco+1 # Bug 1 (fim das linhas passando)
                        eliminarComeco = 0 # Eliminar desde começo

                    if '/*' in i: # Se comentário foi aberto na linha
                        if eliminarFim == eliminarComeco:
                            eliminarFim = eliminarFim+1 # Bug 2 (fim das linhas passando 2)
                        eliminarComeco = i.index('/*')
                        comentarioAberto = True
                    if ('*/' in i) and comentarioAberto: # Se comentário foi fechado na linha
                        if eliminarFim == eliminarComeco+1:
                            eliminarComeco = eliminarComeco-1 # Bug 1 (fim das linhas passando)
                        eliminarFim = i.index('*/')+2
                        comentarioAberto = False
                    i = i[:eliminarComeco] + i[eliminarFim:]
                    if not '/*' in i: # Fim do loop
                        break
                    else:
                        pass
                        # print('=',i,'ABRT=',comentarioAberto)
                if len(i) > 0: 
                    ret.append(i)

        simbolos = ["*","!=","==","=","!",";","[","]","(",")","{","}"]
        for i in range(len(ret)): # Padroniza espaço entre símbolos e nomes
            for simbolo in simbolos:
                ret[i] = ret[i].replace(simbolo, ' %s ' % simbolo)

        for i in range(len(tmpConteudo)): # Elimina múltiplos espaços
            while '  ' in tmpConteudo[i]:
                tmpConteudo[i] = tmpConteudo[i].replace('  ', ' ')

        # Descamuflar strings temporariamente
        tmpConteudo = "\n".join(ret).split("\"")
        for i in range(len(tmpConteudo)):
            if i%2 == 1:
                if tmpConteudo[i] == "$$$$$$$$$$$$":
                    tmpConteudo[i] = strings[i//2]
        tmpConteudo = '\"'.join(tmpConteudo).split('\n')

        return tmpConteudo


