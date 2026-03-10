class Logica:

    def AND(self, a, b):
        return bool(a and b)

    def OR(self, a, b):
        return bool(a or b)

    def NOT(self, a):
        return bool(not a)

    def XOR(self, a, b):
        return bool(a) != bool(b)

    def NAND(self, a, b):
        return not (bool(a) and bool(b))

    def NOR(self, a, b):
        return not (bool(a) or bool(b))

    def XNOR(self, a, b):
        return bool(a) == bool(b)

    def implicacion(self, a, b):
        return (not bool(a)) or bool(b)

    def bi_implicacion(self, a, b):
        return bool(a) == bool(b)