class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabecera = None

    def insertar(self, valor):
        nuevo_nodo =  Nodo(valor)
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
                print(nodo_actual.valor, end = "->")
                nodo_actual = nodo_actual.siguiente
            print("None")

    def eliminar_al_inicio(self):
        if self.cabecera is None:
            print("La LSL está vacía")
        else:
            self.cabecera = self.cabecera.siguiente
            nodo_actual = self.cabecera


    def buscar(self, valor):
        nodo_actual = self.cabecera
        pos = 0
        while nodo_actual:
            if nodo_actual.valor == valor:
                print("Valor encontrado en la posición {:.0f}".format(pos))
                return True
            nodo_actual = nodo_actual.siguiente
            pos += 1
        print("Valor no encontrado")
        return False

    def buscar_binario(self, cabecera, valor):
        nodo_actual = cabecera
        fin = None
        while True:
            h = self.nodo_medio(nodo_actual, fin)
            if h == None:
                return None
            if h.valor == valor:
                return h.valor
            elif h.valor < valor:
                nodo_actual = h.siguiente
            else:
                fin = h
            if not(fin == None or fin != nodo_actual):
                break
            return None
    
    def nodo_medio(self, cabecera, fin):
        if cabecera is None:
            return None
        f = cabecera
        l = cabecera.siguiente
        while l != fin:
            l = l.siguiente
            if l != fin:
                l = l.siguiente
                f = f.siguiente
        return f

             

def main():
    Lista = LSL()
    Lista.insertar(5)
    Lista.insertar(4)
    Lista.insertar(8)
    Lista.insertar(3)
    Lista.mostrar()
    Lista.buscar(4)
    Lista.eliminar_al_inicio()
    Lista.mostrar()
    Lista.eliminar_al_inicio()
    Lista.mostrar()
if __name__ == "__main__":
    main()    