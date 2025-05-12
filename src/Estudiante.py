class Estudiante:
    def __init__(self,identificacion, nombre, edad, materias, uc_aprobadas):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.materias = materias
        self.uc_aprobadas = uc_aprobadas
        self.creditos_totales = 0
    
    def getInfo(self):
        return [self.identificacion, self.nombre, self.edad, self.materias, self.uc_aprobadas]
    