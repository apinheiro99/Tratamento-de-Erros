def dividir(dividendo, divisor):
    # print(divisor.resultado)
    return dividendo / divisor

def testa_divisao(divisor):
    try:
        resultado = dividir (10, divisor)
        print(f"O resultado da divisao de 10 por {divisor} e {resultado}")
    except ZeroDivisionError:
        print("Erro de divisao por zero tratado")

try:
    testa_divisao(0)
except AttributeError:
    print("Erro de atributo tratado")

print("Programa encerrado")