from abc import ABCMeta, abstractclassmethod
from functools import total_ordering

@total_ordering
class Conta(metaclass = ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractclassmethod
    def passa_mes(self):
        pass

    def __str__(self) -> str:
        return f">>Código {self._codigo}\n>>Saldo {self._saldo}"

    def __eq__(self, other):
        if(type(other) != Conta):
            return False
        return self._codigo == other._codigo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

class ContaCorrente(Conta):
    def passa_mes(self):
        self._saldo -=2

class ContaPoupanca(Conta):
    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    def passa_mes(self):
        self._saldo *= 1.05


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self) -> str:
        return f">>Código {self._codigo}\n>>Saldo {self._saldo}"

if __name__ == '__main__':
    conta16 = ContaCorrente(16)
    conta16.deposita(1000)

    conta17 = ContaPoupanca(17)
    conta17.deposita(1000)

    conta18 = ContaInvestimento(18)
    conta18.deposita(1000)

    contas = [conta16, conta17, conta18]
    for conta in contas:
        conta.passa_mes()

    for conta in sorted(contas, reverse = True):
        print(f"{conta}")