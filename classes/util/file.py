import os
import pathlib

class File:
    @staticmethod
    def splitFilePath(filename):
        # return os.path.dirname(filename)
        ret = os.path.split(os.path.abspath(filename))
        return (ret[0]+os.sep,ret[1])

    @staticmethod
    def getAbsPath(orig_file,rel_file):
        return os.path.abspath( os.path.dirname(orig_file)+os.sep+rel_file )

    @staticmethod
    def userPath():
        return str(pathlib.Path().absolute())+os.sep

    @staticmethod
    def arquivoExiste(path):
        return os.path.isfile(path)