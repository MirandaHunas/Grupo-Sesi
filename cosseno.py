def fatorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado


def cosseno(y, termos=20):
    resultado = 0
    for x in range(termos):
        conta = (-1) ** x
        resultado += conta * (y ** (2 * x)) / fatorial(2 * x)
    return resultado


valor = int(input('Digite o valor desejado em graus: '))

radiano = valor * 0.0174533

print(cosseno(radiano))
