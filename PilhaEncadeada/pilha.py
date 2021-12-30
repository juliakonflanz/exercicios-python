# Disciplina de AED 2 - Tarefa de Pilhas (encadeamento)
# Júlia Konflanz Freitas - 142358

class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

    def __repr__(self):
        return "%s -> %s" % (self.dado, self.prox)


class pilha:
    def __init__(self):
        self.topo = None
    
    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def vazia(self):
        if self.topo is None:
           return True
    
    def imprime(self): 
        conteudo = self.topo 
        if conteudo is None:
            print("A lista não tem elementos.")
        while conteudo: 
            print(conteudo.dado)
            conteudo = conteudo.prox
    
    def empilhar(self, dado):
        novo = Nodo(dado)
        if (not self.vazia()):
            novo.prox = self.topo
        self.topo = novo

    def excluir(self):
        if (not self.vazia()):
            aux = self.topo
            self.topo = aux.prox
            del aux
    
    def consultar(self):
        if (not self.vazia()):
            return self.topo.dado

    def destruir(self):
        while (not self.vazia()):
            self.excluir()