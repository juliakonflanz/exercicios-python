from pilha import *

print("\nCRIANDO PILHA\n")
pilha = pilha(5)

print("INSERINDO ELEMENTOS NA PILHA")
for i in range(5):
    pilha.empilhar(i)
    print(repr(pilha))

print("\nCONSULTANDO TOPO DA PILHA")
print(repr(pilha.consultar()))
    
print("\nTOPO DA PILHA REMOVIDO\n")
pilha.excluir()

print("CONSULTANDO TOPO DA PILHA")
print(repr(pilha.consultar()))

print("\nDESTRUINDO PILHA")
pilha.destruir()
print(repr(pilha))


