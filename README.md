# QXCoder-ES
A Python3 code editor based on old Vi.

[![Travis Build Status](https://travis-ci.com/jeimison3/QxCoder-ES.svg?branch=master)](https://travis-ci.com/jeimison3/QxCoder-ES)
[![codecov](https://codecov.io/gh/jeimison3/QxCoder-ES/branch/master/graph/badge.svg)](https://codecov.io/gh/jeimison3/QxCoder-ES)



## O que é o QXCoder? ##
O QXCoder é um editor de código com interface semelhante ao antigo Vi, sendo totalmente escrito em Python3 e com características de uma IDE. Sua principal vantagem está na simplicidade de uso. Conte com a simplicidade dos atalhos de teclado, mas a robustez e praticidade de uma verdadeira IDE.

Para executar o editor, use `./qxcoder [nomeDoArquivo.c]` ou simplesmente `./qxcoder`. Se instalado, use `qxcoder` diretamente.

## Recursos
- Destaque de cores nas principais estruturas. 

## Sobre o software
- Teste(s): Unitário (`via TravisCI`)
- Métrica(s): Cobertura de código (`via codecov`)

## TODO:
- Alternar entre arquivos por janelas.
- Sugestão de código com base nos arquivos do projeto.
- Atalhos para copiar e colar.

### Instalação:
```shell
git clone https://github.com/jeimison3/QxCoder-ES.git
cd QxCoder-ES
./qxcoder [nomeDoArquivo.c]
```


### Desenvolvimento e testes
```shell
cd QxCoder-ES
pip install -r requirements.txt 
```
- Testes podem ser iniciados via `pytest` ou `python3 -m pytest`.
- Testes individuais de classe podem ser feitos via:
```shell
pytest testes/controller/TArquivo.py -s
```

Para inserir novas bibliotecas basta inserir em `requirements.txt`.
