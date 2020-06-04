import curses
from src.input import Input

class Window:

    def __init__(self):
        '''
        Construtor da classe
        '''
        self.inp = None

    def setInput(self, input : Input):
        self.inp = input