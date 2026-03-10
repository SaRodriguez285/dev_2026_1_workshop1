class Stats:
    def promedio(self, numeros):
        if len(numeros) == 0:
            raise ValueError("La lista no puede estar vacía")
        
        return sum(numeros) / len(numeros)

    
    def mediana(self, numeros):
        if len(numeros) == 0:
            raise ValueError("La lista no puede estar vacía")

        nums = sorted(numeros)
        n = len(nums)
        mitad = n // 2

        if n % 2 == 0:
            return (nums[mitad - 1] + nums[mitad]) / 2
        else:
            return nums[mitad]

    
    def moda(self, numeros):
        if len(numeros) == 0:
            raise ValueError("La lista no puede estar vacía")

        frecuencias = {}
        max_freq = 0
        moda = numeros[0]

        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1
            
            if frecuencias[num] > max_freq:
                max_freq = frecuencias[num]
                moda = num

        return moda

    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar de una lista de números.
        Usa la fórmula de desviación estándar poblacional.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La desviación estándar
            
        Ejemplo:
            desviacion_estandar([1, 2, 3, 4, 5]) -> 1.41...
        """
        pass
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        La varianza es el cuadrado de la desviación estándar.
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            float: La varianza
            
        Ejemplo:
            varianza([1, 2, 3, 4, 5]) -> 2.0
        """
        pass
    
    def rango(self, numeros):
        """
        Calcula el rango (diferencia entre el valor máximo y mínimo).
        
        Args:
            numeros (list): Lista de números
            
        Returns:
            number: La diferencia entre max y min
            
        Ejemplo:
            rango([1, 5, 3, 9, 2]) -> 8
        """
        pass