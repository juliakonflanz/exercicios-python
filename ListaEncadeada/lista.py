class Node:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
 
class Lista:
    def __init__(self):
        self.ini = None
    
    def imprime(self): 
        conteudo = self.ini 
        if conteudo is None:
            print("A lista não tem elementos.")
        while conteudo: 
            print(conteudo.dado)
            conteudo = conteudo.prox

    def tamanho(self):
        total = 0
        if self.ini == None:
            return total
        else:
            atual_nodo = self.ini
            while atual_nodo != None:
                total += 1
                atual_nodo = atual_nodo.prox
            return total

    def insere(self, dado):
        novo_nodo = Node(dado)
        if self.ini == None:
            self.ini = novo_nodo
            return
        atual_nodo = self.ini
        while atual_nodo.prox:
            atual_nodo = atual_nodo.prox
        atual_nodo.prox = novo_nodo
        return

    def insereQqrPosicao(self, posicao, dado):
        if posicao == 1:
            novo_nodo = Node(dado)
            novo_nodo.prox = self.ini
            self.ini = novo_nodo
        else:
            i = 1
            atual_nodo = self.ini
            while i < posicao-1 and atual_nodo is not None:
                atual_nodo = atual_nodo.prox
                i = i + 1
            if atual_nodo is None:
                print("Posiçao inválida.")
            else: 
                novo_nodo = Node(dado)
                novo_nodo.prox = atual_nodo.prox 
                atual_nodo.prox  = novo_nodo

    def removeValor(self, valor):
        if self.ini.dado == valor:
            self.ini = self.ini.prox
        else:
            anterior = None
            posterior = self.ini
            while posterior and posterior.dado != valor:
                anterior = posterior
                posterior = posterior.prox                        
            if posterior:                
                anterior.prox = posterior.prox
            else:
                anterior.prox = None

    def buscaPosicao(self, valor):
        if self.ini == None:
            print("Lista vazia.")
            return None
        atual_posicao = 0
        atual_nodo = self.ini
        while atual_nodo != None:
            if atual_nodo.dado == valor:
                print("Dado ",valor," na posição", atual_posicao)
                return atual_nodo
            atual_nodo = atual_nodo.prox
            atual_posicao += 1
        print("Dado ", valor, " não encontrado.")

    def buscaValor(self, posicao):
        if posicao >= self.tamanho() or posicao < 0:
            print("Posição ", posicao, " inválida.")
            return None
        atual_posicao  = 0
        atual_nodo = self.ini
        while atual_nodo != None:
            if atual_posicao == posicao: 
                print("Posição ", posicao," com o valor", atual_nodo.dado)
                return atual_nodo.dado
            atual_nodo  = atual_nodo.prox
            atual_posicao += 1
            
    def inverte(self):
        anterior_nodo = None
        atual_nodo = self.ini
        while atual_nodo != None:
            prox = atual_nodo.prox
            atual_nodo.prox = anterior_nodo
            anterior_nodo = atual_nodo
            atual_nodo = prox
        self.ini = anterior_nodo

    def compara(lista1, lista2):
        tamanho1 = lista1.tamanho()
        tamanho2 = lista2.tamanho()
        if tamanho1 != tamanho2:
            print("As listas não são iguais.")
            return False
        else:
            aux1 = lista1.ini
            aux2 = lista2.ini
            cont = 0
            for i in range(tamanho1):
                if aux1.dado != aux2.dado:
                    cont += 1
                aux1 = aux1.prox
                aux2 = aux2.prox
            if cont > 0:
                print("As listas não são iguais.")
                return False
            else:
                print("Listas iguais")
                return True

    def destruir(self):
        self.dado = None
        self.ini = None
        self.prox = None
        self.tamanho = 0