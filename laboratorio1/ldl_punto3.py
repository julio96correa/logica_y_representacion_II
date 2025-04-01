class Nodo():
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None
        
class LDL():
    def __init__(self):
        self.cabecera = None
        
    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            return

        nodo_actual = self.cabecera
        while nodo_actual.siguiente is not None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = nodo_actual
            
    def mostrar(self):
        nodo_actual = self.cabecera
        while nodo_actual:
            print(nodo_actual.valor, end = "<->")
            nodo_actual = nodo_actual.siguiente
        print("None")

def main():
    # Prueba 1:
    # Generar una LDL = 1 <-> 5 <-> 6 <-> 9 <-> 10 <-> NULL
    # Colocar la función principal para solucionar y la respuesta generada
    Lista = LDL()
    Lista.encolar(1)
    Lista.encolar(5)
    Lista.encolar(6)
    Lista.encolar(9)
    Lista.encolar(10)
    print("Lista 1")
    Lista.mostrar()
    # Prueba 2:
    # Generar una LDL = 8 <-> 8 <-> 10 <-> 10 <-> 20 <-> NULL
    # Colocar la función principal para solucionar y la respuesta generada
    Lista = LDL()
    Lista.encolar(8)
    Lista.encolar(8)
    Lista.encolar(10)
    Lista.encolar(10)
    Lista.encolar(20)
    print("\nLista 2")
    Lista.mostrar()

if __name__ == "__main__":
    main()