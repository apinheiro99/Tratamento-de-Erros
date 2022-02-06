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
        self.saldo =100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

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