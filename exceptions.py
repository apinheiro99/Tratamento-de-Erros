class SaldoInsuficienteError(Exception):
    
    def __init__(self, message="", saldo = None, valor = None, *args):
        self.__saldo = saldo
        self.__valor = valor
        msg = "Saldo insuficiente para efetuar a transacao\n" \
            f"Saldo atual: {self.__saldo}  Valor a ser sacado: {self.__valor}"
        super(SaldoInsuficienteError, self).__init__(message or msg, self.__saldo, self.__valor, *args)