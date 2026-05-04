class Calculadora:
    def calcular(self, primeiro_numero: float, operador: str, segundo_numero: float) -> float:
        if operador == "+":
            return primeiro_numero + segundo_numero

        elif operador == "-":
            return primeiro_numero - segundo_numero

        elif operador == "*":
            return primeiro_numero * segundo_numero

        elif operador == "/":
            if segundo_numero == 0:
                raise ValueError("Não é possível dividir por zero.")
            return primeiro_numero / segundo_numero

        else:
            raise ValueError("Operador inválido.")