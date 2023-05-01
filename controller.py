# COntroller e responsavel pela logica, pela validação

from dal import ProdutosDal
from model import Produtos


# Class de Produtos


class ProdutosController:
    @classmethod
    def cadastrar_produto(cls, nome, quantidade, validade):
        x = ProdutosDal.ler()

        list_est = list(filter(lambda x: x.nome.replace('\n', '') == nome, x))

        if len(list_est) > 0:
            print('Produto existe em nossa base de dados.')

        else:
            produ = Produtos(nome, quantidade, validade)
            ProdutosDal.salvar(produ)
            print('Produto cadastrado com sucesso.')

    @classmethod
    def alterar_produto(cls, prod_alterar, novo_nome, quant_nova, valid_novo):
        estoque = ProdutosDal.ler()

        list_est = list(
            filter(lambda x: x.nome.replace('\n', '') == prod_alterar, estoque)
        )

        for i in range(len(estoque)):
            if estoque[i].nome.replace('\n', '') == prod_alterar:
                del estoque[i]
                break

        with open('produtos.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(
                    i.nome + '|' + i.quantidade + '|' + i.validade
                )
        for i in estoque:
            if not i.nome == novo_nome:
                produto = Produtos(novo_nome, quant_nova, valid_novo)
                ProdutosDal.salvar(produto)
                print('Produto alterado com sucesso.')

    @classmethod
    def remover_produto(cls, nome_remover):
        estoque = ProdutosDal.ler()

        list_estoque = list(
            filter(lambda x: x.nome.replace('\n', '') == nome_remover, estoque)
        )
        if len(list_estoque) == 0:
            print('Produto NÃO existe em estoque')
        else:
            for i in range(len(estoque)):
                if estoque[i].nome.replace('\n', '') == nome_remover:
                    del estoque[i]
                    break
                else:
                    print('produto não contém no estoque.')

            print('Produto removido com sucesso')

            with open('produtos.txt', 'w') as arq:
                for i in estoque:
                    arq.writelines(
                        i.nome + '|' + i.quantidae + '|' + i.validade
                    )
