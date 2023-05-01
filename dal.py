# Dal seria que faz o acesso ao banco de dados, qualquer tipo de armazenamento persistente

from model import Produtos


class ProdutosDal:
    @classmethod
    def salvar(cls, produto: Produtos):
        with open('produtos.txt', 'a') as arq:
            arq.writelines(
                produto.nome
                + '|'
                + produto.quantidade
                + '|'
                + produto.validade
                + '\n'
            )

    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            cls.nome_p = arq.readlines()

        produtos = []

        if len(cls.nome_p) > 0:
            for i in cls.nome_p:
                i = i.split('|')
                produtos.append(Produtos(i[0], i[1], i[2]))

        return produtos

    @classmethod
    def listar_estoque(cls):
        arquivo = open('produtos.txt', 'r')
        listat_est = arquivo.readlines()
        return listat_est
