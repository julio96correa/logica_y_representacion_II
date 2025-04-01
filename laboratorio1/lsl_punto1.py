class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabecera = None
    
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
    
    def mostrar(self):
        if self.cabecera is None:
            print("La LSL está vacía")
        else: 
            nodo_actual = self.cabecera
            while nodo_actual:
                print(nodo_actual.valor, end="->")
                nodo_actual = nodo_actual.siguiente
            print("None")
            
    @staticmethod
    def concatenar(Lista_1, Lista_2):
        nueva_lsl = LSL()
        nodo_actual = Lista_1.cabecera
        while nodo_actual:
            nueva_lsl.insertar(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
            
        nodo_actual = Lista_2.cabecera
        while nodo_actual:
            nueva_lsl.insertar(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
            
        return nueva_lsl
   
    def dividir(self):
        if self.cabecera is None:
            return None, None 
        tortuga = self.cabecera
        liebre = self.cabecera
        while liebre and liebre.siguiente and liebre.siguiente.siguiente:
            tortuga = tortuga.siguiente
            liebre = liebre.siguiente.siguiente
        derecha = LSL()
        derecha.cabecera = tortuga.siguiente
        tortuga.siguiente = None
        izquierda = self
        return izquierda, derecha  
        
    def merge_sort(self):
        if self.cabecera is None or self.cabecera.siguiente is None:
            return self
        izquierda, derecha = self.dividir()
        if not izquierda or not derecha:
            return self
        izquierda = izquierda.merge_sort()
        derecha = derecha.merge_sort()
        return LSL.fusionar(izquierda, derecha)
    
    @staticmethod
    def fusionar(izquierda, derecha):
        lista_ordenada = LSL()
        nodo_izquierdo = izquierda.cabecera
        nodo_derecho = derecha.cabecera
        
        while nodo_izquierdo and nodo_derecho:
            
            if nodo_izquierdo.valor < nodo_derecho.valor:
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

def main():
    
    # Prueba 1:
    # Lista_1 = 7 -> 8 -> 8 -> 1 -> NULL
    # Lista_2 = 2 -> 9 -> 1 -> 4 -> NULL

    print("Prueba 1")
    Lista_1 = LSL()
    Lista_1.insertar(7)
    Lista_1.insertar(8)
    Lista_1.insertar(8)
    Lista_1.insertar(1)
    Lista_1 = Lista_1.merge_sort()
    print("Lista 1")
    Lista_1.mostrar()
    
    Lista_2 = LSL()
    Lista_2.insertar(2)
    Lista_2.insertar(9)
    Lista_2.insertar(1)
    Lista_2.insertar(4)
    print("Lista 2")
    Lista_2.mostrar()
    
    # Colocar la función principal para solucionar y la respuesta generada
    Lista_concatenada = LSL.concatenar(Lista_1, Lista_2)
    print("Lista concatenada:")
    Lista_concatenada.mostrar()
    Lista_concatenada = Lista_concatenada.merge_sort()
    print("Lista ordenada:")
    Lista_concatenada.mostrar()
    
    # Prueba 2:
    # Lista_1 = 10 -> 9 -> 8 -> 7 -> NULL
    # Lista_2 = 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> NULL

    print("\nPrueba 2")
    Lista_1 = LSL()
    Lista_1.insertar(10)
    Lista_1.insertar(9)
    Lista_1.insertar(8)
    Lista_1.insertar(7)
    print("Lista 1")
    Lista_1.mostrar()

    Lista_2 = LSL()
    Lista_2.insertar(6)
    Lista_2.insertar(5)
    Lista_2.insertar(4)
    Lista_2.insertar(3)
    Lista_2.insertar(2)
    Lista_2.insertar(1)
    print("Lista 2")
    Lista_2.mostrar()

    # Colocar la función principal para solucionar y la respuesta generada
    Lista_concatenada = LSL.concatenar(Lista_1, Lista_2)
    print("Lista concatenada:")
    Lista_concatenada.mostrar()
    Lista_concatenada = Lista_concatenada.merge_sort()
    print("Lista ordenada:")
    Lista_concatenada.mostrar()
    
    # Prueba 3:
    # Lista_1 = 5 -> 5 -> 5 -> 5 -> NULL
    # Lista_2 = 6 -> 6 -> 6 -> NULL

    print("\nPrueba 3")
    Lista_1 = LSL()
    Lista_1.insertar(5)
    Lista_1.insertar(5)
    Lista_1.insertar(5)
    Lista_1.insertar(5)
    print("Lista 1")
    Lista_1.mostrar()

    Lista_2 = LSL()
    Lista_2.insertar(6)
    Lista_2.insertar(6)
    Lista_2.insertar(6)
    print("Lista 2")
    Lista_2.mostrar()

    # Colocar la función principal para solucionar y la respuesta generada
    Lista_concatenada = LSL.concatenar(Lista_1, Lista_2)
    print("Lista concatenada:")
    Lista_concatenada.mostrar()
    Lista_concatenada = Lista_concatenada.merge_sort()
    print("Lista ordenada:")
    Lista_concatenada.mostrar()
    
if __name__ == "__main__":
    main()
