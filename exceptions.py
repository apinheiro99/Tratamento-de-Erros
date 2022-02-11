from logging import exception


class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(Exception):
    
    def __init__(self, message="", saldo = None, valor = None, *args):
        self.__saldo = saldo
        self.__valor = valor
        msg = "Saldo insuficiente para efetuar a transacao\n" \
            f"Saldo atual: {self.__saldo}  Valor a ser sacado: {self.__valor}"
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg, self.__saldo, self.__valor, *args)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def valor(self):
        return self.__valor