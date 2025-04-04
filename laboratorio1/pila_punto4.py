"""
Nombre del archivo: pila_punto4.py

Descripción:
    Implementación de una pila que se creará a partir del proceso de desapilar una pila original.

Autores:
    - Julio Cesar Correa Ocampo
    - Diego Alejandro Vergara Ruiz
"""
class Pila:
    """
    Implementación de una estructura de datos tipo pila.

    Atributos:
        V (list): Lista que almacena los elementos de la pila.
        cima (int): Índice del último elemento apilado.
    """
    def __init__(self, n):
        self.V = [None] * n
        self.cima = -1
    
    def pila_vacia(self):
        """
        Verifica si la pila está vacía.
        
        Retorna:
            bool: True si la pila está vacía, False en caso contrario.
        """
        if self.cima == -1:
            return True
        
    def pila_llena(self):
        """
        Verifica si la pila está llena.
        
        Retorna:
            bool: True si la pila está llena, False en caso contrario.
        """
        if self.cima == len(self.V) - 1:
            return True
        
    def apilar(self, valor):
        """
        Agrega un elemento a la pila.
        
        Parámetros:
            valor: Elemento a agregar a la pila.
        """
        if self.pila_llena():
            print("La pila está llena") 
        else: 
            self.cima += 1
            self.V[self.cima] = valor
    
    def desapilar(self):
        """
        Elimina y retorna el elemento en la cima de la pila.
        
        Retorna:
            valor_a_elimnar: Elemento eliminado de la pila o None si la pila está vacía.
        """
        if self.pila_vacia():
            print("La pila está vacía")
            return None
        else:
            valor_a_eliminar = self.V.pop(self.cima)
            self.cima -= 1
            return valor_a_eliminar
    
    @staticmethod
    def crear_pila_nueva(pila_original, n):
        """
        Crea una nueva pila con los elementos de la pila original.
        Se usa método estático ya que se trabaja sobre una pila nueva.
        
        Parámetros:
            pila_original (Pila): Pila a copiar.
            n (int): Tamaño de la nueva pila.
        
        Retorna:
            Pila: Nueva pila con los mismos elementos que la original.
        """
        pila_nueva = Pila(n)
        while pila_original.cima != -1:
            pila_nueva.apilar(pila_original.desapilar())
        return pila_nueva
    
    def mostrar(self):
        print(self.V)
        
def main():
    tamano = int(input("Ingerese el tamaño de la pila:"))
    pila = Pila(tamano)
    
    while not pila.pila_llena():
        
        valor = input("Ingrese un dato: ")
        pila.apilar(valor)
    print("Pila original")
    pila.mostrar()
    nueva_pila = Pila.crear_pila_nueva(pila, tamano)
    print("Pila nueva")
    nueva_pila.mostrar()
    
    # Prueba 1:
    # Lista = [2, 7, 9, 5, 7, 5]
    # Colocar la función principal para solucionar y la respuesta generada
    pila = Pila(6)
    pila.apilar(2)
    pila.apilar(7)
    pila.apilar(9)
    pila.apilar(5)
    pila.apilar(7)
    pila.apilar(5)
    print("\nPila 1")
    pila.mostrar()
    Pila_nueva = Pila.crear_pila_nueva(pila, 6)
    print("Pila nueva")
    Pila_nueva.mostrar()
    
    # Prueba 2:
    # Lista = [1, 1, 1, 1, 1, 1]
    # Colocar la función principal para solucionar y la respuesta generada
    pila = Pila(6)
    pila.apilar(1)
    pila.apilar(1)
    pila.apilar(1)
    pila.apilar(1)
    pila.apilar(1)
    pila.apilar(1)
    print("\nPila 2")
    pila.mostrar()
    Pila_nueva = Pila.crear_pila_nueva(pila, 6)
    print("Pila nueva")
    Pila_nueva.mostrar() 
    
    # Prueba 3:
    # Lista = [5, 5, 7, 7, 1, 1]
    # Colocar la función principal para solucionar y la respuesta generada    
    pila = Pila(6)
    pila.apilar(5)
    pila.apilar(5)
    pila.apilar(7)
    pila.apilar(7)
    pila.apilar(1)
    pila.apilar(1)
    print("\nPila 3")
    pila.mostrar()
    Pila_nueva = Pila.crear_pila_nueva(pila, 6)
    print("Pila nueva")
    Pila_nueva.mostrar() 
    
if __name__ == "__main__":
    main()