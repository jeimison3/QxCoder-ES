class CProcessor:
    @staticmethod
    def getConteudoEntre(tx : str, c:str):
        conteudo = tx.split(c,3)
        if len(conteudo) == 3:
            return conteudo[1]
        else:
            return None
