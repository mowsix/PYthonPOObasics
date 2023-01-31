#La palabra reservada def nos indica que vamos a crear un metodo seguido del nombre
#La palabra reservada self la utilizamos para referirnos al objeto con la estructura self.nombre=algoritmo
#utilizamos __init__ para inicializar
class matematicas:
    def __init__(self):
        self.numero1=45
        self.numero2=45
s=matematicas()
print(s.numero1+s.numero2)

