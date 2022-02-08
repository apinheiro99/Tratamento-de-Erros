def dividir(dividendo, divisor):
    try:
        aux = dividendo / divisor
        return aux
    except:
        print(f"Nao foi possivel dividir {dividendo} por {divisor}")

def testa_divisao(divisor):
        resultado = dividir (10, divisor)
        print(f"O resultado da divisao de 10 por {divisor} e {resultado}")

# Teste 1
try:
    testa_divisao(0)
except AttributeError as E:
    print("Erro de atributo tratado")
    print(E)
    print(E.__class__.__bases__)
except ZeroDivisionError as E:
    print("Erro de divisao por zero tratado")
    print(E)
    print(E.__class__.__bases__)

print("Programa encerrado 1")