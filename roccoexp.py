# Função que calcula uma aproximação de e^x usando a série de Taylor
def exponencial(exp):

    # Define a quantidade de termos da série que serão usados no cálculo
    # Quanto maior o número de termos, maior a precisão
    termos = int(2 * abs(exp))

    # Inicializa o fatorial com 1 (0! = 1)
    fatorial = 1

    # Inicializa a soma com 1, que é o primeiro termo da série
    soma = 1

    # Inicializa o numerador (x^n) com 1
    numerador = 1

    # Loop que calcula os termos da série
    for n in range(1, termos):

        # Calcula x^n multiplicando pelo valor de exp a cada iteração
        numerador *= exp

        # Calcula n! progressivamente
        fatorial *= n

        # Soma o termo atual da série: (x^n / n!)
        soma += numerador / fatorial

    # Retorna o valor final da soma (aproximação de e^x)
    return(soma)


# Solicita ao usuário um valor para calcular e^x
exp = float(input("Digite: "))

# Chama a função exponencial passando o valor digitado
resultado = exponencial(exp)

# Mostra o resultado final
print(resultado)