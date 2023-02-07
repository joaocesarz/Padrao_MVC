# COntroller e responsavel pela logica, pela validação

from dal import ProdutosDal
from model import Produto


class ProdutosController:

    @classmethod
    def cadastrar_produto(cls, nome, quantidade, validade):
        existe = False
        x = ProdutosDal.ler()
        for i in x:
            if i == nome == quantidade == validade:
                existe = True

        if not existe:
            ProdutosDal.salvar(nome == quantidade == validade)
            print('Produto cadastrado com sucesso.')
        else:
            print('Produto Não existe em nossa base de dados.')




    