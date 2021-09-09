from fabrica_fila import FabricaFila

if __name__ == '__main__':
    teste_fabrica = FabricaFila.pega_fila('normal')
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    print(f"{teste_fabrica.chama_cliente(10)}")