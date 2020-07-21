# QXCoder-ES
A Python3 code editor based on old Vi.

[![Travis Build Status](https://travis-ci.com/jeimison3/QxCoder-ES.svg?branch=master)](https://travis-ci.com/jeimison3/QxCoder-ES)

## O que é o QXCoder? ##
O QXCoder é um editor de código com interface semelhante ao antigo Vi, sendo totalmente escrito em Python3 e com características de uma IDE. Sua principal vantagem está na simplicidade de uso. Conte com a simplicidade dos atalhos de teclado, mas a robustez e praticidade de uma verdadeira IDE.

Para executar o editor, use `./main.py [nomeDoArquivo.c]` ou simplesmente `./main.py`

## Recursos
- Destaque de cores nas principais estruturas. 

## TODO:
- Alternar entre arquivos por janelas.
- Sugestão de código com base nos arquivos do projeto.
- Atalhos para copiar e colar.

### Instalação:
```shell
git clone https://github.com/jeimison3/QxCoder-ES.git
cd QxCoder-ES
pip install -r requirements.txt 
```


### Desenvolvedores
- Testes podem ser iniciados via `./testes.py`

Para inserir novas bibliotecas usar `pip freeze > requirements.txt`