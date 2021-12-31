from fila import *
from pilha import *

def organiza():
    print("FILA")
    fila = fila_enc()
    fila.inserir(1)
    print(repr(fila))
    fila.inserir(4)
    print(repr(fila))
    fila.inserir(2)
    print(repr(fila))
    fila.inserir(3)
    print(repr(fila))
    print("\n")

    print("PILHA 1")
    pilha = pilha_enc()
    pilha.empilhar(1)
    print(repr(pilha))
    print("\n")

    print("FILA")
    fila.excluir()
    print(repr(fila))
    print("\n")

    print("PILHA 2")
    pilha2 = pilha_enc()
    pilha2.empilhar(1)
    print(repr(pilha2))
    print("\n")

    print("PILHA 1")
    pilha.excluir()
    pilha.empilhar(4)
    print(repr(pilha))
    print("\n")

    print("PILHA 1")
    pilha.empilhar(1)
    print(repr(pilha))
    print("\n")

    print("PILHA 2")
    pilha2.excluir()
    print(repr(pilha2))
    print("\n")

    print("FILA")
    fila.excluir()
    print(repr(fila))
    print("\n")

    print("PILHA 2")
    pilha2.empilhar(1)
    print(repr(pilha2))
    print("\n")

    print("PILHA 1")
    pilha.excluir()
    print(repr(pilha))
    print("\n")

    print("PILHA 1")
    pilha.empilhar(2)
    print(repr(pilha))
    print("\n")

    print("PILHA 1")
    pilha.empilhar(1)
    print(repr(pilha))
    print("\n")

    print("PILHA 2")
    pilha2.excluir()
    print(repr(pilha2))
    print("\n")

    print("FILA")
    fila.excluir()
    print(repr(fila))
    print("\n")

    print("PILHA 2")
    pilha2.empilhar(1)
    print(repr(pilha2))
    print("\n")

    print("PILHA 2")
    pilha2.empilhar(2)
    print(repr(pilha2))
    print("\n")

    print("PILHA 1")
    pilha.excluir()
    pilha.excluir()
    print(repr(pilha))
    print("\n")

    print("PILHA 1")
    pilha.empilhar(3)
    print(repr(pilha))
    print("\n")

    print("PILHA 1")
    pilha.empilhar(2)
    print(repr(pilha))
    print("\n")

    print("PILHA 1")
    pilha.empilhar(1)
    print(repr(pilha))
    print("\n")

    print("PILHA 2")
    pilha2.destruir()
    print(repr(pilha2))
    print("\n")

    print("FILA")
    fila.excluir()
    print(repr(fila))
    print("\n")

    print("FILA")
    fila.inserir(1)
    print(repr(fila))
    print("\n")

    print("PILHA 1")
    pilha.excluir()
    print(repr(pilha))
    print("\n")

    print("FILA")
    fila.inserir(2)
    print(repr(fila))
    print("\n")

    print("PILHA 1")
    pilha.excluir()
    print(repr(pilha))
    print("\n")

    print("FILA")
    fila.inserir(3)
    print(repr(fila))
    print("\n")

    print("PILHA 1")
    pilha.excluir()
    print(repr(pilha))
    print("\n")

    print("FILA")
    fila.inserir(4)
    print(repr(fila))
    print("\n")

    print("PILHA 1")
    pilha.destruir()
    print(repr(pilha))
    print("\n")

organiza()
