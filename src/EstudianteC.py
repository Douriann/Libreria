class Estudiante:
    def __init__(self,cedula, nombre, edad, carrera, razon_solicitud):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.razon_solicitud = razon_solicitud

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

    def describir_razon(self):
        if self.razon_solicitud == "1":
            razon = "Inclusión de materia"
        elif self.razon_solicitud == "2":
            razon = "Retiro de materia"
        elif self.razon_solicitud == "3":
            razon = "Cambio de carrera"
        else:
            razon = "No especificado"
        print(f"Razón de solicitud: {razon}")
        return razon