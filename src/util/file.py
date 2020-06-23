import os
import pathlib

class File:
    @staticmethod
    def splitFilePath(filename):
        ret = os.path.split(os.path.abspath(filename))
        return (ret[0]+os.sep,ret[1])

    @staticmethod
    def userPath():
        return str(pathlib.Path().absolute())+os.sep