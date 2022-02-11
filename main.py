from pprint import pprint
from exceptions import SaldoInsuficienteError

class Cliente:
    def __init__ (self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0

        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)

        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia (self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser inteiro")

        if value <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero (self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo numero deve ser inteiro")

        if value <= 0:
            raise ValueError("O atributo numero deve ser maior que zero")

        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    def __set_saldo (self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo saldo deve ser inteiro")

        self.__saldo = value

    def trasferir (self, valor, favorecido):
        if valor < 0:
            raise ValueError("O valor transferido nao pode ser negativo")
        self.sacar(valor)
        favorecido.depositar (valor)

    def sacar (self, valor):
        if valor < 0:
            raise ValueError("O valor sacado nao pode ser negativo")

        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError (saldo = self.saldo, valor=valor)

        self.__set_saldo(self.__saldo - valor)
        # self.__saldo -= valor

    def depositar (self, valor):
        self.__set_saldo(self.__saldo + valor)
        # self.__saldo += valor

# #Testando a classe
# cliente = Cliente("Jhon Doe", "123.456.789-00", "Desenvolvedor")

# print(cliente.nome)
# print(cliente.cpf)
# print(cliente.profissao)

# print(cliente.__dict__)

# pprint(cliente.__dict__, width = 40)

# conta_corrente = ContaCorrente(None, "00A", "101")

# #Teste 02

# print("################################")
# conta_corrente = ContaCorrente(None, 100, "101")
# # conta_corrente.agencia = 0
# print(conta_corrente.saldo)
# print(conta_corrente.agencia)

# def main():
#     import sys

#     contas = []
#     while True:
#         try:
#             nome = input("Nome do Cliente:\n")
#             agencia = input("Numero da agencia:\n")
#             numero = input("Numero da conta corrente:\n")
#             cliente = Cliente(nome, None, None)
#             conta_corrente = ContaCorrente(cliente, agencia, numero)
#             contas.append(conta_corrente)
#         except ValueError as E: 
#             print(E.args)
#             sys.exit()
#         except KeyboardInterrupt:
#             print(f"\n\n{len(contas)}(s) contas criadas")
#             sys.exit()

# if __name__ == "__main__":
#     main()

# try:
#     conta_corrente = ContaCorrente(None,400,123456)
#     conta_corrente.depositar(100)
#     print("Saldo:",conta_corrente.saldo)
#     conta_corrente.sacar(110)
#     print("Saldo:",conta_corrente.saldo)
# except SaldoInsuficienteError as E:
#     print(E.args)

import os
os.system("clear")

conta_corrente1 = ContaCorrente(None,400,123456)
conta_corrente2 = ContaCorrente(None,401,212256)
try:
    conta_corrente1.trasferir(500,conta_corrente2)
    print("Saldo conta1: ",conta_corrente1.saldo)
    print("Saldo conta2: ",conta_corrente2.saldo)
except SaldoInsuficienteError as E:
    import traceback
    print(E.saldo)
    print (E.valor)
    print("Excecao do tipo:", E.__class__.__name__)
    traceback.print_exc()