# Arquivo Model, seria a modelagem dos dados. 

class Produto:
    
    def __init__(self, produto, quantidade, validade):  # entidade
        self.produto = produto
        self.quantidade = quantidade
        self.validade = validade
