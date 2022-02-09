from pprint import pprint

class Cliente:
    def __init__ (self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo =100
        self.cliente = cliente
        self.__agencia = agencia
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia (self, value):
        if not isinstance(value, int):
            print("O atributo agencia deve ser inteiro")
            return

        if value <= 0:
            print("O atributo agencia deve ser maior que zero")
            return

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero

    def __set_numero (self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return

        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo

    def __set_saldo (self, value):
        if not isinstance(value, int):
            return
        if value <= 0:
            return

        self.__saldo = value

    def trasferir (self, valor, favorecido):
        favorecido.depositar (valor)

    def sacar (self, valor):
        self.saldo -= valor

    def depositar (self, valor):
        self.saldo += valor

#Testando a classe
cliente = Cliente("Jhon Doe", "123.456.789-00", "Desenvolvedor")

print(cliente.nome)
print(cliente.cpf)
print(cliente.profissao)

print(cliente.__dict__)

pprint(cliente.__dict__, width = 40)

conta_corrente = ContaCorrente(None, "00A", "101")

#Teste 02

print("################################")
conta_corrente.agencia = 0
print(conta_corrente.saldo)
print(conta_corrente.agencia)