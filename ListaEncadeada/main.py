from lista import *

lista = Lista()
print("\n\tINSERINDO SEQUENCIALMENTE NA LISTA")
lista.insere(2)
lista.insere(7)
lista.insere(1)
lista.insere(8)
lista.imprime()

print("\n\n\tTAMANHO DA LISTA")
lista.tamanho()

print("\n\n\tINSERINDO NA POSIÇÃO 2 DA LISTA")
lista.insereQqrPosicao(2,3)
lista.imprime()

print("\n\n\tREMOVENDO VALOR 1 DA LISTA")
lista.removeValor(1)
lista.imprime()

print("\n\n\tBUSCANDO AS POSIÇÕES DOS ELEMENTOS DA LISTA")
lista.buscaPosicao(2)
lista.buscaPosicao(3)
lista.buscaPosicao(7)
lista.buscaPosicao(8)
print("\n\tTeste para elemento não existente:")
lista.buscaPosicao(9)

print("\n\n\tBUSCANDO OS ELEMENTOS DAS POSIÇÕES DA LISTA")
lista.buscaValor(0)
lista.buscaValor(1)
lista.buscaValor(2)
lista.buscaValor(3)
print("\n\tTeste para posição não existente:")
lista.buscaValor(4)

print("\n\n\tINVERTENDO LISTA")
lista.inverte()
lista.imprime()

print("\n\tCRIANDO SEGUNDA LISTA")
print("\n\tINSERINDO SEQUENCIALMENTE NA LISTA 2")
lista2 = Lista()
lista2.insere(8)
lista2.insere(7)
lista2.insere(3)
lista2.insere(2)
lista2.imprime()

print("\n\tCOMPARANDO LISTAS")
lista.compara(lista, lista2)

print("\n\n\tDESTRUINDO LISTA 1")
lista.destruir()
lista.imprime()

print("\n\n\tDESTRUINDO LISTA 2")
lista2.destruir()
lista2.imprime()