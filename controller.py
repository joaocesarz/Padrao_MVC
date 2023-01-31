# COntroller e responsavel pela logica, pela validação

from dal import ProdutosDal
from model import Produto


class ProdutosController:

    @classmethod
    def cadastrar_produto(cls, produto, quantidade, validade):


        ProdutosDal.salvar(Produto(produto, quantidade, validade))
        return True

    