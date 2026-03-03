class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        resultado = []
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado

    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1


    def eliminar_duplicados(self, lista):
        resultado = []
        for elemento in lista:
            existe = False
            for guardado in resultado:
                if elemento == guardado and type(elemento) == type(guardado):
                    existe = True
                    break
            if not existe:
                resultado.append(elemento)
        return resultado


    def merge_ordenado(self, lista1, lista2):
        resultado = []
        i = 0
        j = 0

        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1

        while i < len(lista1):
            resultado.append(lista1[i])
            i += 1

        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado
    
    def rotar_lista(self, lista, k):
        n = len(lista)
        if n == 0:
            return lista
        
        k = k % n
        resultado = []
        
        for i in range(n - k, n):
            resultado.append(lista[i])
            
        for i in range(0, n - k):
            resultado.append(lista[i])
            
        return resultado

    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        return suma_esperada - suma_real
    

    def es_subconjunto(self, conjunto1, conjunto2):
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True

    
    def implementar_pila(self):
        pila = []

        def push(elemento):
            pila.append(elemento)

        def pop():
            if pila:
                return pila.pop()
            return None

        def peek():
            if pila:
                return pila[-1]
            return None

        def is_empty():
            return len(pila) == 0

        return {
            "push": push,
            "pop": pop,
            "peek": peek,
            "is_empty": is_empty
        }

    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass