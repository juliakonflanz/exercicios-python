from produto import *
from lista import *

produtoA = produto("1005", 122020)
produtoB = produto("8491", 112021)
produtoC = produto("2254", 102021)

print("\n\tCRIANDO LISTA")
lista = Lista(7)
if (lista.inserir(1, produtoA)):
    print(lista)
if (lista.inserir(2, produtoB)):
    print(lista)
if (lista.inserir(3, produtoC)):
    print(lista)

print("\n\tINSERINDO PRODUTOS NA LISTA")
lista.inserir(4,produtoC)
print(lista)
lista.inserir(4,produtoC)
print(lista)
lista.inserir(4,produtoC)
print(lista)
lista.inserir(4,produtoC)
print(lista)

print("\n\tBUSCANDO DADOS DO PRODUTO")
meuproduto = lista.buscar(1)
print(meuproduto)

print("\n\tINSERÇÃO OTIMIZADA")
lista2 = Lista(7)
if (lista2.inserirOtimizado(1,produtoA)):
    print(repr(lista2))
if (lista2.inserirOtimizado(2,produtoB)):
    print(lista2)
if (lista2.inserirOtimizado(3,produtoC)):
    print(lista2)
if (lista2.inserirOtimizado(1,produtoB)):
    print(lista2)
if (lista2.inserirOtimizado(2,produtoC)):
    print(lista2)
if (lista2.inserirOtimizado(4,produtoC)):
    print(lista2)
if (lista2.inserirOtimizado(5,produtoC)):
    print(lista2)
