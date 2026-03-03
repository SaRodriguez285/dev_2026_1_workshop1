class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.strip().lower()
        jugador2 = jugador2.strip().lower()

        opciones = {"piedra", "papel", "tijera"}

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }

        if reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    
    def ta_te_ti_ganador(self, tablero):
        lineas = []

        lineas.extend(tablero)

        for col in range(3):
            lineas.append([tablero[0][col], tablero[1][col], tablero[2][col]])

        lineas.append([tablero[0][0], tablero[1][1], tablero[2][2]])
        lineas.append([tablero[0][2], tablero[1][1], tablero[2][0]])

        for linea in lineas:
            if linea == ["X", "X", "X"]:
                return "X"
            if linea == ["O", "O", "O"]:
                return "O"

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"


    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        pass
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        pass