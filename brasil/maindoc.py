from cpf import CPF
from cnpj import CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return CPF(documento)
        elif len(documento) == 14:
            return CNPJ(documento)

if __name__ == "__main__":
    newDocumento = Documento.cria_documento("13079052692")
    newDocumento2 = Documento.cria_documento("13079052692123")
    print(f"{newDocumento}")
    print(f"{newDocumento2}")