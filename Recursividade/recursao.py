# 1) Implementação iterativa e recursiva de operação de soma de elementos.
#    Por exemplo: se v = [1, 2, 3, 10], o método deve retornar 16.
def somaElementosIterativo(valores):
    tam = len(valores)
    cont = 0
    soma = 0
    while (cont<tam):
        soma = soma + valores[cont]
        cont = cont + 1
    return soma

def somaElementosRecursivo(valores):
    if (len(valores) == 1):
        return valores[0]
    else:
        return valores[0] + somaElementosRecursivo(valores[1:])

# 2) Implementação iterativa e recursiva de um método que retorna o fatorial de um número natural.
def fatorialIterativo(valor):
    fatorial = 1
    while (valor>0):
        fatorial = fatorial * valor
        valor = valor - 1
    return fatorial

def fatorialRecursivo(valor):
    if (valor == 1):
        return 1
    else:
        return valor * fatorialRecursivo(valor - 1)

# 3) Implementação iterativa e recursiva do cálculo de Fibonacci.
def fibonacciIterativo(termos):
    if (termos == 2):
        return 1
    else:
        n_1, n_2, n, cont = 0, 1, 1, 1
        while (cont < termos):
            n = n_1 + n_2
            n_1 = n_2
            n_2 = n
            cont = cont + 1
    return n

def fibonacciRecursivo(n):
    if (n <= 1):
        return n
    else:
        return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

# 4) Implementação recursiva de método de soma de dígitos.
#    Por exemplo: soma dos dígitos 14 deve retornar 5.
def somaDigitosRecursivo(valor):
    if (valor == 0):
        return 0
    else:
        return (valor % 10) + somaDigitosRecursivo(valor // 10)
