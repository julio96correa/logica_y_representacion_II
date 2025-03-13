class Nodo: 
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LSLC:
    def __init__(self):
        self.fin = None
        self.cabecera = None

    def insertarconNULL(self, valor):
        if self.fin != None:
            return self.fin
        nuevo_nodo = Nodo(valor)
        self.fin = nuevo_nodo
        self.fin.siguiente = self.fin
        self.cabecera = self.fin
        return self.fin
    
    def insertaralInicio(self, valor):
        if self.fin == None:
            return self.insertarconNULL(valor)
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.fin.siguiente
        self.fin.siguiente = nuevo_nodo
        return self.fin
    
    def insertaralFinal(self, valor):
        if self.fin == None:
            return self.insertarconNULL(valor)
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.siguiente
        self.fin.siguiente = nuevo_nodo
        self.fin = nuevo_nodo
        return self.fin
    
    def mostrar(self):
        if self.fin == None:
            return print("LSLC está vacía")
        nodo_actual = self.fin.siguiente
        while nodo_actual is not None:
            print(nodo_actual.valor, end = "->")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.fin.siguiente:
                break
        return None



def main():
        Lista = LSLC()
        Lista.insertaralInicio(7)
        Lista.insertaralInicio(6)
        Lista.insertaralInicio(5)
        Lista.mostrar()

if __name__ == "__main__":
        main()
