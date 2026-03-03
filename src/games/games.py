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


    import random
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        if longitud <= 0:
            return []

        return [random.choice(colores_disponibles) for _ in range(longitud)]

    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and
                0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False

        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        return True