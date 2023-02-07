# Dal seria que faz o acesso ao banco de dados, qualquer tipo de armazenamento persistente

from model import Produto


class ProdutosDal:

    @classmethod             # método de uma classe que pode ser chamado diretamente, sem ser instânciado. ele  recebe o parametro cls
    def salvar(cls, produto: Produto):
        with open('produtos.txt', 'a') as arq:
            arq.writelines(produto.nome + ' ' + produto.quantidade + ' ' + produto.validade)
            arq.writelines('\n')



    @classmethod
    def ler(cls):
        with open('produtos.txt', 'r') as arq:
            cls.nome = arq.readlines()

        
        produtos = []


        if len(cls.nome) > 0:
            for i in cls.nome:
                produtos.append(i)

        return produtos

        
