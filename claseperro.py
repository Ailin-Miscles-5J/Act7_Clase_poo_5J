print("Programacion POO")
#deinicion de clases
class Perro:
    #Funciones dentro de la clase
    nombre="Body"
    edad=4
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self,nombre,edad):
        print(f"  Nombre:  {nombre}  Edad:  {edad}")


#zona de creacion de objto
pitbull=Perro()

#zona de uso de objetos

pitbull.Datos_perro("Boby",4)
pitbull.morder()