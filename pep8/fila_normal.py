class Fila_normal:
    codigo = 0
    fila = []
    clientes_atendidos = []
    senha_atual : str = ""

    def gera_senha(self) -> None:
        self.senha_atual = f"NM{self.codigo}"

    def reseta_fila(self):
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa : str) -> str:
        cliente_atual : str = self.fila.pop(0)
        return(F"Cleinte atual: {cliente_atual}, dirija-se ao caixa: {caixa}")