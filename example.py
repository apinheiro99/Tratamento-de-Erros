def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError ("dividir() deve receber apenas argumentos inteiros")
    
    try:
        aux = dividendo / divisor
    except:
        print(f"Nao foi possivel dividir {dividendo} por {divisor}")
        raise

    return aux

def testa_divisao(divisor):
        resultado = dividir (10, divisor)
        print(f"O resultado da divisao de 10 por {divisor} e {resultado}")

# Teste 1
try:
    testa_divisao(1.2)
except AttributeError as E:
    print("Erro de atributo tratado")
    print(E)
    print(E.__class__.__bases__)
except ZeroDivisionError as E:
    print("Erro de divisao por zero tratado")
    print(E)
    print(E.__class__.__bases__)
except Exception as E:
    print("Erro geral")
    print(E)
    print(E.__class__.__bases__)

print("Programa encerrado 1")

try:
    print("O fluxo esta aqui")
    raise ValueError
except Exception:
    print("Agora ele foi para ca")
print("E enfim ele continua...")