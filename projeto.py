import os

produtos = [
    {'id': 1, 'nome': "Notebook Galaxy book4", 'preço': 3400.00, "estoque": 6},
    {'id': 2, 'nome': "Teclado Gamer Redragon", 'preço': 165.67, "estoque": 11},
    {'id': 3, 'nome': "Mouse Gamer sem fio Logitech", 'preço': 469.99, "estoque": 2},
    {'id': 4, 'nome': "Headset Gamer Logitech", 'preço': 348.89, "estoque": 1},
    {'id': 5, 'nome': "Microfone dinâmico FIFINE", 'preço': 270.48, "estoque": 7},
    {'id': 6, 'nome': "Câmera Webcam Logitech C920e", 'preço': 320.00, "estoque": 3},
    {'id': 7, 'nome': "Monitor LG 24'' Full HD", 'preço': 899.90, "estoque": 4},
    {'id': 8, 'nome': "Impressora Multifuncional HP", 'preço': 759.99, "estoque": 5},
    {'id': 9, 'nome': "Cadeira Gamer ThunderX3", 'preço': 1100.00, "estoque": 2},
    {'id': 10, 'nome': "Mesa Digitalizadora Wacom", 'preço': 490.50, "estoque": 3},
]

carrinho = []

def cor(txt, cor_code="0"):
     return f"\033[{cor_code}m{txt}\033[0m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu():
    print(cor('\n🛒 MENU PRINCIPAL', "1;36"))
    print(cor("1.", "1;33"),' Ver catálogo')
    print(cor("2.", "1;33"), 'Adicionar ao carrinho')
    print(cor("3.", "1;33"), 'Ver carrinho')
    print(cor("4.", "1;33"), 'Remover item')
    print(cor("5.", "1;33"),' Finalizar')
    print(cor("6.", "1;33"), 'Sair')


def exibir_catalogo():
    for p in produtos:
         print(f"ID: {p['id']} | {p['nome']} - R$ {p['preço']} | Estoque: {p['estoque']}")

def encontrar_produto(id_escolhido):
    for produto in produtos:
        if produto['id'] == id_escolhido:
                return produto
    return None
            
def adicionar_ao_carrinho():
    try:
        id_escolhido = int(input('Digite o ID do produto: '))
        produto = encontrar_produto(id_escolhido)

        if not produto:
            print('Produto não encontrado.')
            return

        if produto['estoque'] == 0:
                print('Produto sem estoque.')
                return

        quantidade = int(input("Quantidade desejada: "))
        
        if quantidade <= 0:
            print('Quantidade inválida')
            return

        if quantidade > produto['estoque']:
            print('Estoque insuficiente')
            return

        for item in carrinho:
                if item['id'] == id_escolhido:
                    item['quantidade'] += quantidade
                    break
            
        else:
            carrinho.append({
                'id': produto['id'],
                'nome': produto['nome'],
                'preço': produto['preço'],
                'quantidade': quantidade 
            })

        produto['estoque'] -= quantidade
        print(f'{quantidade} unidade(s) adicionada(s) ao carrinho.')

    except ValueError:
        print("Digite apenas valores válidos.")

def ver_carrinho():
    if not carrinho:
        print('Seu carrinho está vazio')
        return
    for item in carrinho:
        print(f'{item["nome"]} | {item["quantidade"]} un. | R$ {item["preço"] * item["quantidade"]:.2f}')
    
def remover_do_carrinho():
    try:
        id_remover = int(input('Digite o ID do produto que deseja remover'))

        for item in carrinho:
            if item['id'] == id_remover:
                quantidade = int(input('Quantidade a remover: '))    
                if quantidade >= item['quantidade']:
                            carrinho.remove(item)          
                else:
                    item['quantidade'] -= quantidade
                produto = encontrar_produto(id_remover)   
                if produto:
                    produto['estoque'] += quantidade
                print('Item removido.')
                return
        print('Item não encontrado no carrinho.')
    except ValueError:
        print('Entrada inválida.')
                           
def finalizar_compra():
        if not carrinho:
            print('Seu carrinho está vazio.')
            return
        total = sum(item['preço'] * item['quantidade'] for item in carrinho)
        print('Resumo da compra:')
        for item in carrinho:
            print(f'{item["nome"]} | {item["quantidade"]} un. | R$ {item["preço"] * item["quantidade"]:.2f}')
        print('-'*40)
        print(f'Total: R$ {total:.2f}')
        carrinho.clear()
        print('Compra finalizada com sucesso!')
           
while True:
    exibir_menu()
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        exibir_catalogo()
    elif escolha == '2':
        adicionar_ao_carrinho()
    elif escolha == '3':
         ver_carrinho()
    elif escolha == '4':
         remover_do_carrinho()
    elif escolha == '5':
         finalizar_compra()
    elif escolha == '6':
         print('Encerrando...')
         break
    else:
         print('Opção inválida.')