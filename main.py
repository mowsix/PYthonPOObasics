# CLASES Y OBJETOS

class profesiones:  # clase
    # Objetos que pertenecen a la clase persona
    # Atributos de la clase
    Bomberos = 30
    policias = ""
    profesores = 2


trabajo = profesiones()
print(profesiones.profesores)

#======================================================================================

#CREAR OBJETOS FUERA DE LA CLASE
class nombres:
    pass #esto indica que es el final de la clase
victor=nombres()
maria=nombres()
sara=nombres()
#ESTRUCTURA-> Objeto.atributo=valor
victor.edad=27
victor.pais="Colombia"
maria.edad=41
maria.pais="Argentina"
print(victor.edad)

#======================================================================================

#METODOS
#La palabra reservada def nos indica que vamos a crear un metodo seguido del nombre
#La palabra reservada self la utilizamos para referirnos al objeto con la estructura self.nombre=algoritmo
#utilizamos __init__ para inicializar
class matematicas:
    def __init__(self):
        self.numero1=45
        self.numero2=45
s=matematicas()
print(s.numero1+s.numero2)

#======================================================================================

#Agregar variables a un solo metodo
class Calculadora:
    def __init__(self,n1,n2):
        self.suma=n1+n2
        self.resta=n1-n2
        self.multiplicacion=n1*n2
operacion=Calculadora(13,78)
print(operacion.multiplicacion)

#======================================================================================

#Metodos de acceso GET Y SET
class cuenta:
    def __init__(self, pro, sal, mon):
        self.__propietario=pro
        self.__saldo=sal
        self.__moneda=mon

    #Metodo GET =======
    def get_Propietario(self):
        return self.__propietario

    def get_Saldo(self):
        return self.__saldo

    def get_Moneda(self):
        return self.__moneda

    #Metodo SET =============

    def set_Moneda(self, moneda):
        self.__moneda=moneda

cuenta1=cuenta("Oscar",1500,"dolares")

print(cuenta1.get_Propietario())
print(cuenta1.get_Saldo())
cuenta1.set_Moneda("Pesos")
print(cuenta1.get_Moneda())







#Herencia


#Funciones con atributos

