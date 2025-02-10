class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.hijos = []  # Lista de hijos (otros objetos Persona)

    #Funcion para agregar un objeto Persona a la lista de otro objeto Persona
    def agregarHijo(self, hijo):
        self.hijos.append(hijo)

    #Funcion para imprimir la info de los miembros de todo el arbol
    def mostrarArbol(self, generacion=0):
        #Cada generacion aumenta la sangría 
        print("  " * generacion + f"- {self.nombre} (Edad: {self.edad})")
        for hijo in self.hijos:
            hijo.mostrarArbol(generacion + 1)

# Funcion para crear una nueva persona a traves de un input del usuario
def crearPersona():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    return Persona(nombre, edad)

# Funcion recursiva para agregar hijos a cada hijo del abuelo y mas hijos y asi
def agregarMiembros(padre):
    while True:  
        opcion = input(f"¿Desea agregar un hijo a {padre.nombre}? (s/n): ").lower()
        if opcion == "s":
            hijo = crearPersona()
            padre.agregarHijo(hijo)
            agregarMiembros(hijo) #Se vuelve a llamar a si misma para agregar nietos, bisnietos y asi  
        elif opcion == "n":
            break 
        else:
            print("Por favor, ingrese 's' o 'n'.")

# Crear el ancestro principal (seria la raiz del árbol)
print("Bienvenido, empieza ingresando al mayor ancestro de tu arbol genealogico")
ancestroMayor = crearPersona()

agregarMiembros(ancestroMayor)

# Mostrar todo el arboll al final
print("\nÁrbol Genealógico:")
ancestroMayor.mostrarArbol()
