class CNPJ:
    def __init__(self, documento):
        self.documento = documento
        if self.validacao(documento):
            self.CNPJ = documento
        else:
            raise ValueError(f"CNPJ: {self.documento} Invalido!!!")

    def validacao(self, documento):
        if len(documento) == 14:
            return True
        else:
            return False

    def fatiaCNPJ(self):
        self.fatia1 = self.documento[:2]
        self.fatia2 = self.documento[2:5]
        self.fatia3 = self.documento[5:8]
        self.fatia4 = self.documento[8:12]
        self.fatia5 = self.documento[12:]
        self.CNPJ_formatado = f"{self.fatia1}.{self.fatia2}.{self.fatia3}/{self.fatia4}-{self.fatia5}"
        return self.CNPJ_formatado

    def __str__(self):
        return f"CNPJ: {self.fatiaCNPJ()}"


if __name__ == "__main__":
    newCNPJ = CNPJ("35379823800011")
    print(f"{newCNPJ}")
    
    

