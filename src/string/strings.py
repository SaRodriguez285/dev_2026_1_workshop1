class Strings:

    
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]

    
    def invertir_cadena(self, texto):
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado

    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0

        for char in texto:
            if char in vocales:
                contador += 1

        return contador

    
    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0

        for char in texto:
            if char.isalpha() and char not in vocales:
                contador += 1

        return contador

    
    def es_anagrama(self, texto1, texto2):
        texto1 = texto1.replace(" ", "").lower()
        texto2 = texto2.replace(" ", "").lower()

        return sorted(texto1) == sorted(texto2)

    
    def contar_palabras(self, texto):
        palabras = texto.split()
        return len(palabras)

    
    def palabras_mayus(self, texto):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if palabra:
                resultado.append(palabra[0].upper() + palabra[1:].lower())

        return " ".join(resultado)

    
    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio_anterior = False

        for char in texto:
            if char == " ":
                if not espacio_anterior:
                    resultado += char
                espacio_anterior = True
            else:
                resultado += char
                espacio_anterior = False

        return resultado.strip()

    
    def es_numero_entero(self, texto):
        if texto == "":
            return False

        if texto[0] == "-":
            texto = texto[1:]

        if texto == "":
            return False

        for char in texto:
            if char < '0' or char > '9':
                return False

        return True

    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""

        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                nuevo = (ord(char) - base + desplazamiento) % 26 + base
                resultado += chr(nuevo)
            else:
                resultado += char

        return resultado

    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        pass
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        pass