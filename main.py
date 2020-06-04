from src.window import Window
from src.input import Input

if __name__ == '__main__':
    tela = Window()
    entrada = Input()

    tela.setInput(entrada)
    print(tela)
