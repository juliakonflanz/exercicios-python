class tabela():
    def __init__(self,tamanhoMax):
        self.chave = [None] * (tamanhoMax + 1)
        self.valor = [None] * (tamanhoMax + 1)
        self.li = 1
        self.ls = tamanhoMax
        self.ini = self.li -1
        self.fim = self.ls + 1
        self.inserirOrdned = True
    
    def __repr__(self):
        string = ""
        if (not self.vazia()):
            for i in range (0,self.fim):
                string += str(self.chave[i]) + ": " + str(self.valor[i]) + "\n"
        return string

    def tamanho(self):
        if (self.vazia() == False):
            return (self.fim - self.ini - 1)
        else:
            return False

    def vazia(self):
        return self.ini < self.li or self.fim > self.ls

    def cheia(self):
        return (self.ini == self.li and self.fim == self.ls)

    def inserir(self, chave, valor, ordened=True):
        posicao = self.busca(chave,False)
        if (posicao > 0):
            self.valor[posicao] = valor
        elif (not self.cheia()):
            if (self.vazia()):
                self.ini = self.li
                self.fim = self.li
            else:
                self.fim +=1

            self.chave[self.fim] = chave
            print("Produto: {0} | Lote: {1} | Posição: {2}".format(chave, valor, self.fim))
            self.valor[self.fim] = valor
            if ordened ==True:
                self.inserirOrd()
            else:
                self.inserirOrdned = False
        else:
            print("Tabela cheia!")

    def inserirOrd(self):
            for i in range(self.ini,self.fim+1):
                auxchave = self.chave[i]
                auxvalor = self.valor[i]
                x = i
                while ((x >0) and (str(auxchave) < str(self.chave[x - 1]))):
                    self.valor[x] = self.valor[x - 1]
                    self.chave[x] = self.chave[x - 1]
                    x -= 1
                self.chave[x] = str(auxchave)
                self.valor[x]  = str(auxvalor)

    def cosultar(self, chave):
        posicao = self.busca(chave, False)
        if (posicao > 0):
            return self.valor[posicao]
        else:
            return False

    def buscaLinear(self, chave):
        a = -1
        if not (self.vazia()):
            for i in range(self.ini, self.fim + 1):
                if (self.chave[i] == chave):
                    a = i
                else:
                    pass
            if a != -1:
                #print(a)
                return a
            else:
                return -1
        else:
            return -1

    def buscaBinaria(self, chave): 
        comeco = self.ini
        fim = self.fim 
        if self.inserirOrdned == False :
            print("Não ordenado, iniciando ordenação.")
            self.inserirOrd()
        while(comeco <= fim):
            meio = (comeco + fim) // 2
            if (self.chave[meio] == chave):
                return meio
            elif(self.chave[meio] > chave):
                fim = meio - 1
            else:
                comeco = meio + 1
        return -1

    def busca(self, chave, bin):
        if bin == True:
            return self.buscaBinaria(chave)
        else:
            return self.buscaLinear(chave)

    def excluir(self, chave):
        posicao = self.busca(chave, False)
        if not posicao ==-1:
            for i in range(posicao,self.fim):
                self.chave[i] = self.chave[i+1]
                self.valor[i] = self.valor[i+1]
            self.fim -=1
            print("Excluído!")
        else:
            print("Sem Sucesso.")
            return False

    def destruir(self):
        self.ini = self.li - 1
        self.fim = self.ls + 1    