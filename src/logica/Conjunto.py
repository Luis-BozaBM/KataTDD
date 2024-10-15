class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):

        #Se cambio False por None (rojo -> verde)
        if len(self.__conjunto) == 1:
            return(self.__conjunto[0])
        else:
            return None