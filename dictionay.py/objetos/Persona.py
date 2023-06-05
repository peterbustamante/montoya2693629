class Persona:
    def __init__(self,nombre,documento):
        #print ('se instancion un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.telefono
        self.__curso

    def setNombre(self):
        return self.__nombre

    def getNombre(self):
        return self.__nombre

    def setDocumento(self,nombre):
        return self.__documento
    def getDocumento(self):
        return self.__documento

    def setCurso(self):
        return self.__curso
    def getCurso(self):
        return self.__curso