class Lista:
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1

    def __repr__(self):
        string = "[ini "
        for i in range(self.ini, self.fim + 1):
            string = string + " -> " + str(self.vetor[i])
        return string + "]\n"

    def vazia(self):
        return self.ini == -1 or self.fim == -1

    def tamanho(self):
        if self.vazia():
            return 0
        else:
            return self.fim - self.ini + 1

    def inserir(self, posicao, dado):
        if ((self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.tamanho()+1):
            if (self.vazia()):
               self.ini = self.max // 2
               self.fim = self.max // 2
            elif (self.fim != self.max - 1):
                for i in range(self.fim, self.ini + posicao -2, -1):
                    self.vetor[i+1] = self.vetor[i]
                self.fim = self.fim + 1
            else:
                for i in range(self.ini, self.ini + posicao):
                    self.vetor[i-1] = self.vetor[i]
                self.ini = self.ini - 1
            self.vetor[self.ini + posicao - 1] = dado
            return True
        else:
            return False

    def remover(self, posição):
        if((posição > self.fim - self.ini) or (posição < 0)):
            print("Posição invalida.")
        else:
            self.vetor[self.ini + posição] = None

    def buscar(self, posicao):
        if not self.vazia():
            return self.vetor[self.ini + posicao - 1]
            
    def destruir(self):
        self.vetor = None
        self.ini = 0
        self.fim = -1
        self.tamanho = 0
    
    def inserirOtimizado(self, posicao, dado):
        if ((self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.tamanho()+1):
            if (self.vazia()):
               self.ini = self.max // 2
               self.fim = self.max // 2
            elif (self.ini == 0 or(posicao > self.tamanho() // 2 and self.fim != self.max -1)):
                for i in range(self.fim, self.ini + posicao -2, -1):
                    self.vetor[i+1] = self.vetor[i+1]
                self.fim = self.fim + 1
            else:
                for i in range(self.ini, self.ini + posicao - 1):
                    self.vetor[i-1] = self.vetor[i]
                self.ini = self.ini - 1
            self.vetor[self.ini + posicao - 1] = dado
            return True
        else:
            return False
