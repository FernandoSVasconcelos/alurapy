import requests

class CEP:
    def __init__(self, cep):
        self.cep = cep
        self.valida_cep()

    def valida_cep(self):
        if len(self.cep) == 8:
            return True
        else:
            raise ValueError(f"CEP: {self.cep} INVALIDO")

    def acessa_cep(self):
        req = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        return req.json()

    def __str__(self):
        js = self.acessa_cep()
        return (f"CEP: {js['cep']}\nRUA: {js['logradouro']}\nBAIRRO: {js['bairro']}\nCIDADE: {js['localidade']}")

if __name__ == "__main__":
    cep = input(f"Digite seu cep: ")
    newCEP = CEP(cep)
    print(newCEP)