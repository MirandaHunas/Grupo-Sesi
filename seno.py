print('----- LOG -----')

def fatorial(n):
    #comeca com 1 pois e a base do fatorial
    resultado = 1
 
    #ele vai receber um bloco de codigo e vai contar de 1 ate n
    for i in range(1, n + 1):
        #ele vai multiplicar acumulando, por exemplo n = 4  | 1 x 1 x 2 x 3 x 4
        resultado *= i

    return resultado
    
# definiu termos = 10 pois e um numero equilibrado para boa aproximacao
def seno(x, termos = 10):
    #variavel para guardar o resultado
    soma = 0

    #vai repetir quantas vezes o termos for chaamado
    for n in range (termos): 
        # vai gerar 1, 3, 4, 5, 7 | Pq e a formula do seno usa pra potencias impares
        expoente = 2 * n + 1

        #ele vai alternar o sinal | n = 0 + 1 n 1 - 1 | vai alternar entre + e -
        sinal = (-1) ** n
        #vai montar cada parte da formula
        termo = sinal * (x ** expoente) / fatorial(expoente)
        #vai somar tudo                
        soma += termo
        
    return soma
    
x = float(input('Digite o valor de x (em radianos): '))
termos = int(input('Digite a quantidade de termos da série: '))

resultado = seno(x, termos)

print("Seno aproximado:", resultado)