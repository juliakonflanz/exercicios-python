import tabela as tb

dado = tb.tabela(5)
print("CRIANDO TABELA")
#dado.inserir("produto","lote")
dado.inserir("1","150721")
dado.inserir("2","050821")
dado.inserir("3","190821")
dado.inserir("4","200821")
dado.inserir("5","270821")
print("-"*60)

print("TESTANDO INSERÇÃO MAIOR QUE A TABELA")
dado.inserir("6","310821")
print("-"*60)

print("IMPRIMINDO TABELA")
print(dado.__repr__())
print("-"*60)

print("TESTANDO FUNÇÕES DE BUSCA")
print("Posição {0} por Busca Linear".format(dado.busca("2",False)))
print("Posição {0} por Busca Binária".format(dado.busca("4",True)))
print("Posição {0} por Busca Binária".format(dado.busca("10",True)))
print("-"*60)

print("REMOVENDO ITENS")
print("Remocao do item: 3")
dado.excluir("3")
print("Remocao do item : 10")
dado.excluir("10")
print("-"*60)

print("IMPRIMINDO TABELA")
print(dado.__repr__())
print("-"*60)

print("DESTRUINDO TABELA...")
dado.destruir()
print("-"*60)

print("TESTANDO FUNÇÃO TAMANHO")
print("Tamanho da tabela : {0}".format(dado.tamanho()))
print("-"*60)