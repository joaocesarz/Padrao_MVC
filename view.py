# view fica com a interface grafica

from dal import ProdutosDal
from controller import ProdutosController


print('=============== LISTA DE ESTOQUE DE COMPRAS ===============')
print()
print()

while True:
    decisao = input('Digite [I]nserir [A]pagar [L]istar [S]air: ').lower()


    if decisao == 's':
        break


    elif decisao == 'i':
        nome = input('Nome do Produto: ').upper()
        quantidade = input('Quantidade do Produto: ' )
        validade = input('Difigite a validade do produto: ').replace('/', '')
        ProdutosController.cadastrar_produto(nome=nome, quantidade=quantidade, validade=validade)



    elif decisao == 'l':
        mostrar = ProdutosDal.ler()
        for i in mostrar:
            print(i, end=(''))


    elif decisao == 'a':
        ...

        