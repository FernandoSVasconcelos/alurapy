from fila_normal import Fila_normal
from fila_prioritaria import FilaPrioritaria


if __name__ == '__main__':
    fila_teste = FilaPrioritaria()
    fila_teste.atualiza_fila()
    fila_teste.atualiza_fila()
    fila_teste.atualiza_fila()

    print(f"{fila_teste.chama_cliente(10)}")
    print(f"{fila_teste.chama_cliente(1)}")
    print(f"{fila_teste.estatistica('10/01/1993', 198, 'detail')}")