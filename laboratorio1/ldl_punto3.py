class Nodo():
    """
    Representa un nodo de una lista doblemente enlazada.
    
    Atributos:
        valor (int): Dato almacenado en el nodo.
        anterior (Nodo): Referencia al nodo anterior en la lista.
        siguiente (Nodo): Referencia al siguiente nodo en la lista.
    """
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None
        
class LDL():
    """
    Implementa una Lista Doblemente Enlazada (LDL) con operación de encolar.
    """
    def __init__(self):
        self.cabecera = None
        self.cola = None
        
    def encolar(self, valor):
        """
        Agrega un nuevo nodo al final de la lista, siguiendo la lógica de una cola.
        
        Parámetros:
            valor: Dato a insertar en la lista.
        """
        nuevo_nodo = Nodo(valor)
        if self.cola is None:
            self.cabecera = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
            
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