def dividir(dividendo, divisor):
    return dividendo / divisor

def testa_divisao(divisor):
    try:
        resultado = dividir (10, divisor)
        print(f"O resultado da divisao de 10 por {divisor} e {resultado}")
    except ZeroDivisionError:
        print("Erro de divisao por zero tratado")