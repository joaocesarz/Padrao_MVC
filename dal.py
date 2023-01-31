# Dal seria que faz o acesso ao banco de dados, qualquer tipo de armazenamento persistente

from model import Produto


class ProdutosDal:

    @classmethod             # método de uma classe que pode ser chamado diretamente, sem ser instânciado. ele  recebe o parametro cls
    def salvar(cls, produto: Produto):
        with open('produtos.txt', 'a') as arq:
            arq.write(produto.produto + ' ' + produto.quantidade + ' ' + produto.validade + '\n')



    @classmethod
    def ler(cls, produto: Produto):
        with open('produto.txt', 'r') as arq:
            arq.writelines()
        
