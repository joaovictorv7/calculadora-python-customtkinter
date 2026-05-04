import customtkinter as ctk
from calculadora import Calculadora


class CalculadoraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("330x470")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.calculadora = Calculadora()

        self.numero_atual = ""
        self.expressao = ""
        self.valores = []

        self.criar_interface()

    def criar_interface(self):
        self.display = ctk.CTkEntry(
            self,
            width=290,
            height=60,
            font=("Arial", 28),
            justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        self.display.insert(0, "0")

        botoes = [
            ("C", 1, 0), ("⌫", 1, 1), ("/", 1, 2), ("*", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("-", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("+", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("=", 4, 3),
            ("0", 5, 0), (".", 5, 1)
        ]

        for texto, linha, coluna in botoes:
            botao = ctk.CTkButton(
                self,
                text=texto,
                width=65,
                height=55,
                font=("Arial", 20),
                command=lambda valor=texto: self.clicar(valor)
            )
            botao.grid(row=linha, column=coluna, padx=7, pady=7)

    def clicar(self, valor):
        if valor in "0123456789.":
            self.adicionar_numero(valor)

        elif valor in ["+", "-", "*", "/"]:
            self.adicionar_operador(valor)

        elif valor == "=":
            self.calcular_resultado()

        elif valor == "C":
            self.limpar()

        elif valor == "⌫":
            self.apagar()

    def adicionar_numero(self, valor):
        if valor == "." and "." in self.numero_atual:
            return

        self.numero_atual += valor
        self.expressao += valor
        self.atualizar_display()

    def adicionar_operador(self, operador):
        if self.numero_atual == "":
            return

        self.valores.append(float(self.numero_atual))
        self.valores.append(operador)

        self.numero_atual = ""
        self.expressao += operador

        self.atualizar_display()

    def calcular_resultado(self):
        if self.numero_atual == "":
            return

        self.valores.append(float(self.numero_atual))

        try:
            resultado = self.valores[0]

            posicao = 1

            while posicao < len(self.valores):
                operador = self.valores[posicao]
                proximo_numero = self.valores[posicao + 1]

                resultado = self.calculadora.calcular(
                    resultado,
                    operador,
                    proximo_numero
                )

                posicao += 2

            self.expressao = str(resultado)
            self.numero_atual = str(resultado)
            self.valores = []

        except ValueError:
            self.expressao = "Erro"
            self.numero_atual = ""
            self.valores = []

        self.atualizar_display()

    def limpar(self):
        self.numero_atual = ""
        self.expressao = ""
        self.valores = []
        self.atualizar_display()

    def apagar(self):
        if self.expressao == "":
            return

        ultimo_caractere = self.expressao[-1]
        self.expressao = self.expressao[:-1]

        if ultimo_caractere in "0123456789.":
            self.numero_atual = self.numero_atual[:-1]

        self.atualizar_display()

    def atualizar_display(self):
        self.display.delete(0, "end")

        if self.expressao == "":
            self.display.insert(0, "0")
        else:
            self.display.insert(0, self.expressao)


if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()