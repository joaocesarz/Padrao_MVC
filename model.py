# Arquivo Model, seria a modelagem dos dados.


class Produtos:
    def __init__(self, nome, quantidade, validade):  # entidade
        self.nome = nome
        self.quantidade = quantidade
        self.validade = validade
