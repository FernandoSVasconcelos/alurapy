from fila_base import FilaBase
from constantes import CODIGO_NORMAL

class FilaNormal(FilaBase):

    def gera_senha(self) -> None:
        self.senha_atual = f"{CODIGO_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa : int) -> str:
        cliente_atual : str = self.fila.pop(0)
        return(F"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}")