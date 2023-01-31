# CLASES Y OBJETOS

class profesiones:  # clase
    # Objetos que pertenecen a la clase persona
    # Atributos de la clase
    Bomberos = 30
    policias = ""
    profesores = 2


trabajo = profesiones()
print(profesiones.profesores)

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

