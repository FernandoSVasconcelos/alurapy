class CPF:
    def __init__(self, documento):
        self.documento = documento
        if self.validacao(documento):
            self.cpf = documento
        else:
            raise ValueError(f"CPF: {self.documento} Invalido!!!")

    def validacao(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def fatiaCpf(self):
        self.fatia1 = self.documento[:3]
        self.fatia2 = self.documento[3:6]
        self.fatia3 = self.documento[6:9]
        self.fatia4 = self.documento[9:]
        self.cpf_formatado = f"{self.fatia1}.{self.fatia2}.{self.fatia3}-{self.fatia4}"
        return self.cpf_formatado

    def __str__(self):
        return f"CPF: {self.fatiaCpf()}"


if __name__ == "__main__":
    newCpf = CPF("13079052692")
    print(f"{newCpf}")
    

