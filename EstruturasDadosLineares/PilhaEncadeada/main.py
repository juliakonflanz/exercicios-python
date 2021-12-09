from pilha import *

print("\nCRIANDO PILHA\n")
pilha = pilha()

print("INSERINDO ELEMENTOS NA PILHA")
for i in range(5):
    pilha.empilhar(i)
    print(pilha.imprime)

print("\nCONSULTANDO TOPO DA PILHA")
print(pilha.consultar())
    
print("\nTOPO DA PILHA REMOVIDO\n")
pilha.excluir()

print("IMPRIMINDO PILHA")
print(pilha.imprime)

print("\nDESTRUINDO PILHA")
pilha.destruir()
print(pilha.imprime)


