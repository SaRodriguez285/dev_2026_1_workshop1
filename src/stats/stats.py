import math

class Stats:

    def promedio(self, numeros):
        if not numeros:
            return 0
        return float(sum(numeros) / len(numeros))


    def mediana(self, numeros):
        if not numeros:
            return 0

        nums = sorted(numeros)
        n = len(nums)
        mitad = n // 2

        if n % 2 == 0:
            return float((nums[mitad - 1] + nums[mitad]) / 2)
        else:
            return float(nums[mitad])


    def moda(self, numeros):
        if not numeros:
            return 0

        frecuencias = {}

        for num in numeros:
            frecuencias[num] = frecuencias.get(num, 0) + 1

        max_freq = max(frecuencias.values())

        for num in numeros:
            if frecuencias[num] == max_freq:
                return num


    def varianza(self, numeros):
        if not numeros:
            return 0

        media = self.promedio(numeros)

        suma = 0
        for x in numeros:
            suma += (x - media) ** 2

        return suma / len(numeros)


    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0

        return math.sqrt(self.varianza(numeros))


    def rango(self, numeros):
        if not numeros:
            return 0

        return max(numeros) - min(numeros)