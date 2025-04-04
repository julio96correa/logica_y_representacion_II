class Nodo():
    """
    Representa un nodo de una lista doblemente enlazada (LDL).

    Atributos:
        valor: Dato almacenado en el nodo.
        anterior (Nodo): Referencia al nodo anterior en la lista.
        siguiente (Nodo): Referencia al siguiente nodo en la lista.
    """
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.siguiente = None

class LDL():
    """
    Implementa una Lista Doblemente Enlazada (LDL).
    """
    def __init__(self):
        self.cabecera = None

    def insertar(self, valor):
        """
        Inserta un nuevo nodo al final de la lista.

        Parámetros:
            valor (int): Dato a insertar en la lista.
        """
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            return
        nodo_actual = self.cabecera
        while nodo_actual.siguiente is not None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = nodo_actual

    def dividir(self):
        """
        Divide la lista en dos mitades.

        Retorna:
            tupla: Dos listas LDL (izquierda y derecha).
        """
        if self.cabecera is None:
            return None, None
        tortuga = self.cabecera
        liebre = self.cabecera 
        while liebre.siguiente and liebre.siguiente.siguiente:
            tortuga = tortuga.siguiente
            liebre = liebre.siguiente.siguiente
        derecha = LDL()
        derecha.cabecera = tortuga.siguiente
        if derecha.cabecera:
            derecha.cabecera.anterior = None
        tortuga.siguiente = None
        izquierda = self
        return izquierda, derecha

    def merge_sort(self, descendente=False):
        """
        Ordena la lista enlazada usando Merge Sort.

        Parámetros:
            descendente (bool): Indica si el orden debe ser descendente.

        Retorna:
            LDL: Lista ordenada.
        """
        if self.cabecera is None or self.cabecera.siguiente is None:
            return self
        izquierda, derecha = self.dividir()
        izquierda = izquierda.merge_sort(descendente) if izquierda else None
        derecha = derecha.merge_sort(descendente) if derecha else None
        return LDL.fusionar(izquierda, derecha, descendente)

    @staticmethod
    def fusionar(izquierda, derecha, descendente):
        """
        Fusiona dos listas ordenadas en una sola lista ordenada.
        Se usa @staticmethod ya que se trabaja sobre una lista nueva.
        
        Parámetros:
            izquierda (LDL): Primera lista ordenada.
            derecha (LDL): Segunda lista ordenada.
            descendente (bool): Indica si el orden debe ser descendente.

        Retorna:
            LDL: Lista resultante de la fusión ordenada.
        """
        lista_ordenada = LDL()
        nodo_izquierdo = izquierda.cabecera if izquierda else None
        nodo_derecho = derecha.cabecera if derecha else None

        while nodo_izquierdo and nodo_derecho:
            if (nodo_izquierdo.valor < nodo_derecho.valor) != descendente:
                lista_ordenada.insertar(nodo_izquierdo.valor)
                nodo_izquierdo = nodo_izquierdo.siguiente
            else:
                lista_ordenada.insertar(nodo_derecho.valor)
                nodo_derecho = nodo_derecho.siguiente

        while nodo_izquierdo:
            lista_ordenada.insertar(nodo_izquierdo.valor)
            nodo_izquierdo = nodo_izquierdo.siguiente

        while nodo_derecho:
            lista_ordenada.insertar(nodo_derecho.valor)
            nodo_derecho = nodo_derecho.siguiente

        return lista_ordenada
    
    def eliminar(self, valor):
        """
        Elimina el primer nodo con el valor dado en la lista.

        Parámetros:
            valor (int): Dato a eliminar en la lista.
        """
        nodo_actual = self.cabecera
        
        if nodo_actual is None:
            return
        
        if nodo_actual.valor == valor:
            self.cabecera = nodo_actual.siguiente
            if self.cabecera:
                self.cabecera.anterior = None
                return
        
        while nodo_actual:
            if nodo_actual.valor == valor:
                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                return
            nodo_actual = nodo_actual.siguiente
            

    def eliminar_repetidos(self):
        """
        Elimina los nodos con valores repetidos en la lista.
        """
        nodo_actual = self.cabecera
        while nodo_actual:
            if nodo_actual.siguiente is None:
                return
            if nodo_actual.valor == nodo_actual.siguiente.valor:
                self.eliminar(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
            
    def mostrar(self):
        nodo_actual = self.cabecera
        while nodo_actual:
            print(nodo_actual.valor, end=" <-> ")
            nodo_actual = nodo_actual.siguiente
        print("None")
        

def main():
    # Prueba 1:
    # Lista = 10 <-> 8 <-> 8 <-> 8 <-> 9 <-> NULL

    Lista = LDL()
    Lista.insertar(10)
    Lista.insertar(8)
    Lista.insertar(8)
    Lista.insertar(8)
    Lista.insertar(9)
    print("Lista 1")
    Lista.mostrar()
    # Colocar la función principal para solucionar y la respuesta generada
    Lista = Lista.merge_sort()
    print("Ordenamiento ascendente")
    Lista.mostrar()
    Lista = Lista.merge_sort(descendente=True)
    print("Ordenamiento descendente")
    Lista.mostrar()
    Lista.eliminar_repetidos()
    print("Lista sin repetidos")
    Lista.mostrar()

    # Prueba 2:
    # Lista = 1 <-> 1 <-> 1 <-> 1 <-> 1 <-> NULL

    Lista = LDL()
    Lista.insertar(1)
    Lista.insertar(1)
    Lista.insertar(1)
    Lista.insertar(1)
    Lista.insertar(1)
    print("\nLista 2")
    Lista.mostrar()

    # Colocar la función principal para solucionar y la respuesta generada
    Lista = Lista.merge_sort()
    print("Ordenamiento ascendente")
    Lista.mostrar()
    Lista = Lista.merge_sort(descendente=True)
    print("Ordenamiento descendente")
    Lista.mostrar()
    Lista.eliminar_repetidos()
    print("Lista sin repetidos")
    Lista.mostrar()
    
    # Prueba 3:
    # Lista = 8 <-> 7 <-> 6 <-> -4 <-> -4 <-> -3 <-> -2 <-> -1 <-> NULL

    Lista = LDL()
    Lista.insertar(8)
    Lista.insertar(7)
    Lista.insertar(6)
    Lista.insertar(-4)
    Lista.insertar(-4)
    Lista.insertar(-3)
    Lista.insertar(-2)
    Lista.insertar(-1)
    print("\nLista 3")
    Lista.mostrar()

    # Colocar la función principal para solucionar y la respuesta generada
    Lista = Lista.merge_sort()
    print("Ordenamiento ascendente")
    Lista.mostrar()
    Lista = Lista.merge_sort(descendente=True)
    print("Ordenamiento descendente")
    Lista.mostrar()
    Lista.eliminar_repetidos()
    print("Lista sin repetidos")
    Lista.mostrar()

if __name__ == "__main__":
    main()