class pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [None] * tamanho
        self.lim = tamanho - 1
        self.base = 0
        self.topo = self.base - 1
    
    def __repr__(self):
        return "[" + str(self.topo) + "]"
        
    def empilhar(self, dado):
     if (self.topo < self.lim):
         self.topo += 1
         self.vetor[self.topo] = dado

    def excluir(self):
        if(self.topo < self.base):
            print("Erro. Pilha vazia.")
        else:
           self.topo = self.vetor[self.topo - 1]           

    def consultar(self):
        if(self.topo < self.base):
            print("Erro. Pilha vazia.")
        else:
            return self.vetor[self.topo]

    def destruir(self):
        self.topo = self.base = None

