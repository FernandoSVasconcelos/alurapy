import re

class Telefone:
    def __init__(self, numero):
        self.numero = numero
        self.padrao = re.compile("(35)(9)[0-9]{8}")
        self.valida_numero()

    def valida_numero(self):
        self.busca = self.padrao.search(self.numero)
        if self.busca:
            print(f"Número: {self.numero} está OK")
        else:
            raise ValueError(f"Número {numero} não é valido")

    def mask_numero(self):
        maskpt1 = self.numero[:2]
        maskpt2 = self.numero[2:3]
        maskpt3 = self.numero[3:]
        return f"Telefone: ({maskpt1}) {maskpt2} {maskpt3}"

    def __str__(self):
        return self.mask_numero()

if __name__ == "__main__":
    numero = input("Digite o Número: ")
    newTelefone = Telefone(numero)
    print(newTelefone)
