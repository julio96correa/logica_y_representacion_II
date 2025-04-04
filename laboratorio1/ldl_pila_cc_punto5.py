"""
Nombre del archivo: ldl_pila_cc_punto5.py

Descripción:
    Implementación de una ldl utilizando cola circular,
    se usa lógica de colas para encolar y de pilas para desapilar.

Autores:
    - Julio Cesar Correa Ocampo
    - Diego Alejandro Vergara Ruiz
"""
class Nodo:
    """
    Representa un nodo en una lista doblemente enlazada circular.
    
    Atributos:
        dato: Valor almacenado en el nodo.
        siguiente (Nodo): Referencia al siguiente nodo en la lista.
        anterior (Nodo): Referencia al nodo anterior en la lista.
    """
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class PilaListaDoble:
    """
    Implementación de una pila utilizando una lista doblemente enlazada circular.

    Atributos:
        cabeza (Nodo): Referencia al primer nodo de la pila.
        final (Nodo): Referencia al último nodo de la pila.
    """
    def __init__(self):
        self.cabeza = None  
        self.final = None  
    
    def encolar(self, dato):
        """
        Agrega un elemento a la pila usando la lógica de colas.
        
        Parámetros:
            dato: Valor a insertar en la pila.
        """
        nuevo_nodo = Nodo(dato)
        if self.final is None: 
            self.cabeza = self.final = nuevo_nodo
            self.cabeza.siguiente = self.cabeza.anterior = self.cabeza
        else:
            nuevo_nodo.anterior = self.final
            nuevo_nodo.siguiente = self.cabeza
            self.final.siguiente = nuevo_nodo
            self.cabeza.anterior = nuevo_nodo
            self.final = nuevo_nodo  
    
    def desapilar(self):
        """
        Elimina y retorna el último elemento insertado en la pila ahora sí usando 
        lógica de pilas.
        
        Retorna:
            dato_eliminado: Dato eliminado de la pila o None si está vacía.
        """
        if self.final is None:
            print("La pila está vacía")
            return None
        dato_eliminado = self.final.dato
        if self.cabeza == self.final: 
            self.cabeza = self.final = None
        else:
            self.final = self.final.anterior
            self.final.siguiente = self.cabeza
            self.cabeza.anterior = self.final
        return dato_eliminado
    
    def mostrar(self):
        if self.cabeza is None:
            print("La pila está vacía")
            return
        nodo_actual = self.cabeza
        while True:
            print(nodo_actual.dato, end="<-->")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                break
        print("(circular)")
        
Lista_pila_cc = PilaListaDoble()
Lista_pila_cc.encolar(8)    
Lista_pila_cc.encolar(1)    
Lista_pila_cc.encolar(2)    
Lista_pila_cc.encolar(4)    
Lista_pila_cc.encolar(4)    
Lista_pila_cc.encolar(3)    
Lista_pila_cc.encolar(9)    
Lista_pila_cc.encolar(1)    
Lista_pila_cc.encolar(4)    
Lista_pila_cc.encolar(7)    
Lista_pila_cc.mostrar()
Lista_pila_cc.desapilar()
Lista_pila_cc.desapilar()
Lista_pila_cc.desapilar()
Lista_pila_cc.mostrar()