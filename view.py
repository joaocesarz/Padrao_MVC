# view fica com a interface grafica

from dal import ProdutosDal
from controller import ProdutosController


print('=============== LISTA DE ESTOQUE DE COMPRAS =================')
print()
print()

while True:
    decisao = input(
        'Digite [1]Inserir [2]Alterar [3]Apagar [4]Listar [5]Sair: '
    )
    try:
        decisao = int(decisao)
        match decisao:

            case 5:
                break

            case 1:
                nome = input('Nome do Produto: ').upper()
                quantidade = input('Quantidade do Produto: ')
                validade = input('Difigite a validade do produto: ')
                ProdutosController.cadastrar_produto(
                    nome=nome, quantidade=quantidade, validade=validade
                )

            case 2:
                alterar = input(
                    'Digite o nome do produto que deseja alterar: '
                ).upper()
                print()
                print('Dados para alteração')
                novo_nome = input('Nome do produto: ').upper()
                nova_quant = input('Digite a quantidade: ')
                nova_valid = input('DIgite data de validade: ')
                ProdutosController.alterar_produto(
                    prod_alterar=alterar,
                    novo_nome=novo_nome,
                    quant_nova=nova_quant,
                    valid_novo=nova_valid,
                )

            case 4:
                mostrar = ProdutosDal.listar_estoque()
                for i in mostrar:
                    print()
                    print(i, end=(''))
                    print()

            case 3:
                remover_prod = input(
                    'Digite o nome do produto que deseja remover: '
                ).upper()
                ProdutosController.remover_produto(nome_remover=remover_prod)
    except:
        print('Opção inválida...')
        continue
