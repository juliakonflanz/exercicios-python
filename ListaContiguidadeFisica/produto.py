class produto:
    def __init__(self):
        self.codigo = None
        self.lote = None

    def __init__(self, codigo, lote):
        self.codigo = codigo
        self.lote = lote

    def __repr__(self):
        return "Codigo: " + self.codigo + ", Lote: " + str(self.lote)
    
    def getCodigo(self):
        return self.codigo
    
    def getLote(self):
        return self.lote

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setLote(self, lote):
        self.lote = lote 