class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def __repr__(self):
        return str(self.dado) + " --> " + str(self.prox)


class fila_enc:
    def __init__(self):
        self.ini = None
        self.fim = None
    
    def __repr__(self):
        return "[ini --> " + str(self.ini) + "]"

    def vazia(self):
        return self.ini == None
    
    def inserir(self,dado):
        novo = Nodo(dado)
        if self.vazia():
            self.ini = novo
        else:
            self.fim.prox = novo
        self.fim = novo

    def excluir(self):
        if (not self.vazia()):
            self.ini = self.ini.prox

    def consultar(self):
        if (not self.vazia()):
            return self.ini.dado

    def destruir(self):
        while (not self.vazia()):
            self.excluir()
