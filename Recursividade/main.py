from recursao import *

print("1) SOMA DE ELEMENTOS DE UMA LISTA OU VETOR")
valores = [1,2,3,10]
print("Método iterativo: ", somaElementosIterativo(valores))
print("Método recursivo: ", somaElementosRecursivo(valores))

print("\n2) FATORIAL DE UM NÚMERO NATURAL")
valor = 5
print("Método iterativo: ", fatorialIterativo(valor))
print("Método recursivo: ", fatorialRecursivo(valor))

print("\n3) SEQUÊNCIAS DE FIBONACCI")
termos = 10
print("Método iterativo: ", fibonacciIterativo(termos))
print("Método recursivo: ", fibonacciRecursivo(termos))

print("\n4) SOMA DOS DÍGITOS DE UM NÚMERO NATURAL")
valor = 14
print("Método recursivo: ", somaDigitosRecursivo(valor))