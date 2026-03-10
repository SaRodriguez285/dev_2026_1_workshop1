class Matrix:

    def suma_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")
        
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")
        
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles para multiplicación")

        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(B)):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            resultado.append(fila)
        
        return resultado


    def multiplicar_escalar(self, matriz, escalar):
        return [[elemento * escalar for elemento in fila] for fila in matriz]


    def transpuesta(self, matriz):
        return [list(fila) for fila in zip(*matriz)]


    def es_cuadrada(self, matriz):
        return len(matriz) == len(matriz[0])


    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        
        return matriz == self.transpuesta(matriz)


    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz debe ser cuadrada")
        
        return sum(matriz[i][i] for i in range(len(matriz)))


    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz debe ser 2x2")
        
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]


    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("La matriz debe ser 3x3")
        
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]

        return a*e*i + b*f*g + c*d*h - (c*e*g + b*d*i + a*f*h)


    def identidad(self, n):
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


    def diagonal(self, matriz):
        """
        Extrae los elementos de la diagonal principal de una matriz cuadrada.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            list: Lista con los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 5, 9]
            diagonal([[3, 0], [0, 7]]) -> [3, 7]
        """
        pass

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal
        (todos los elementos fuera de la diagonal principal son cero).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es diagonal, False en caso contrario

        Ejemplo:
            es_diagonal([[3, 0], [0, 7]]) -> True
            es_diagonal([[1, 2], [0, 4]]) -> False
        """
        pass

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz rotada 90 grados en sentido horario

        Ejemplo:
            rotar_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
            rotar_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        pass

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.

        Args:
            matriz (list): Matriz (lista de listas)
            valor: Valor a buscar en la matriz

        Returns:
            list: Lista de tuplas (fila, columna) con las posiciones del valor.
                  Retorna lista vacía si no se encuentra.

        Ejemplo:
            buscar_en_matriz([[1, 2, 3], [4, 2, 6], [7, 8, 2]], 2) -> [(0, 1), (1, 1), (2, 2)]
            buscar_en_matriz([[1, 2], [3, 4]], 9) -> []
        """
        pass
