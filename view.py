# view fica com a interface grafica


from controller import ProdutosController


print('=============== LISTA DE ESTOQUE DE COMPRAS ===============')
print()
print()

while True:
    decisao = input('Digite [I]nserir [A]pagar [L]istar [S]air: ').lower()


    if decisao == 's':
        break


    if decisao == 'i':
        produto = input('Nome do Produto: ').upper()
        quantidade = input('Quantidade do Produto: ' )
        validade = input('Difigite a validade do produto: ').replace('/', '')

        if ProdutosController.cadastrar_produto(produto, quantidade, validade):
            print('Produto cadastrado com sucesso!')
        else:
            print('Digite valores valídos.')



    if decisao == 'l':
        ...


    if decisao == 'a':
        ...

        