class Nodo():

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class LDL():

    def __init__(self):
        self.cabecera = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabecera
        nuevo_nodo.anterior = None
        if self.cabecera is not None:
            self.cabecera.anterior = nuevo_nodo
        self.cabecera = nuevo_nodo

    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            return
        nodo_actual = self.cabecera
        while nodo_actual.siguiente != None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = nodo_actual

    def mostrar(self):
        nodo_actual = self.cabecera
        while nodo_actual:
            print(nodo_actual.valor, end = "<-->")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def insertar_cualquier_posicion(self, valor):
        nodo_actual = self.cabecera
        pos = 0
        while nodo_actual:
            if nodo_actual.valor == valor:
                lugar = int(input("Dónde desea insertar el valor: \n1. Atrás\n2. Adelante"))

def main():
    lista = LDL()
    lista.insertar_al_inicio(5)
    lista.insertar_al_inicio(6)
    lista.insertar_al_inicio(10)
    lista.mostrar()

    lista.insertar_al_final(8)
    lista.insertar_al_final(9)
    lista.mostrar()

if __name__ == "__main__":
    main()       