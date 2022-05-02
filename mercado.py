from typing import List, Dict
from time import sleep
from models.produtos import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('\n===================================')
    print('===========Bem vindo(a)============')
    print('============= KK Shop =============')
    print('===================================')

    print('selecione uma opção abaixo:')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar Produto')
    print('6 - Sair do sistema')

    opcao: int = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(5)
        exit(0)
    else:
        print('Opção inválida!')
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('--------------------')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    novo_produto: Produto = Produto(nome, preco)
    produtos.append(novo_produto)

    print(f'O produto {novo_produto.nome} foi cadastrado com sucesso!')
    sleep(5)
    menu()

def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de Produtos')
        print('--------------------')

        for produto_item in produtos:
            print(produto_item)
            print('...........')
            sleep(1)
            menu()
    else:
        print('Ainda não existem produtos cadastrados!')
        sleep(2)
        menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho')
        print('------------------------------------------------------------')
        print('--------------Lista de Produtos Disponíveis-----------------')

        for produto in produtos:
            print(produto)
            print('........................................')
            sleep(1)

        codigo: int = int(input())
        produto_escolhido: Produto = pega_produto_codigo(codigo)

        if produto_escolhido:
            if len(carrinho) > 0:
                existe_item: bool = False

                for item in carrinho:
                    quantidade = item.get(produto_escolhido)
                    if quantidade > 0:
                        item[produto_escolhido] = quantidade + 1
                        print(f'O produto {produto_escolhido.nome} agora possui {quantidade + 1} no carrinho!')
                        existe_item = True
                        menu()

                if not existe_item:
                    prod = {produto_escolhido: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto_escolhido} foi adicionado ao carrinho!')
                    sleep(3)
                    menu()

            else:
                item = {produto_escolhido: 1}
                carrinho.append(item)
                print(f'O produto {produto_escolhido.nome} foi adicionado ao carrinho!')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado:')
            sleep(2)
            menu()

    else:
        print('Não existem produtos cadastrados!')
        sleep(2)
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')
        print('----------------------')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('----------------------')
                sleep(2)
    else:
        print('Não existem produtos no carrinho!')
        sleep(2)
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print(f'\nProdutos do carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('---------------------')
        print(f'O valor da sua compra é {formata_float_str_moeda(valor_total)}.')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Seu carrinho está vazio!')
        sleep(2)
        menu()


def pega_produto_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
