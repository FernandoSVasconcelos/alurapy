from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

if __name__ == '__main__':
    teste_fabrica = FabricaFila.pega_fila('prioritaria')
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    teste_fabrica.atualiza_fila()
    print(f"{teste_fabrica.chama_cliente(10)}")
    print(f"{teste_fabrica.estatistica(EstatisticaResumida('20/03/2025', 120))}")