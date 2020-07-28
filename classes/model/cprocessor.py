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


        # Descamuflar strings temporariamente
        tmpConteudo = "\n".join(ret).split("\"")
        for i in range(len(tmpConteudo)):
            if i%2 == 1:
                if tmpConteudo[i] == "$$$$$$$$$$$$":
                    tmpConteudo[i] = strings[i//2]
        
        simbolos = ["*","!=","==","=","!",";","[","]","(",")","{","}"]
        for i in range(len(tmpConteudo)): # Padroniza espaço entre símbolos e nomes
            for simbolo in simbolos:
                tmpConteudo[i] = tmpConteudo[i].replace(simbolo, ' %s ' % simbolo)

        for i in range(len(tmpConteudo)): # Elimina múltiplos espaços
            while '  ' in tmpConteudo[i]:
                tmpConteudo[i] = tmpConteudo[i].replace('\t', ' ')
                tmpConteudo[i] = tmpConteudo[i].replace('  ', ' ')
        
        # Retorna ao formato original
        tmpConteudo = '\"'.join(tmpConteudo).split('\n')

        return tmpConteudo


