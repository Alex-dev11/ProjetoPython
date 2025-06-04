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

while True:
    print('\nMENU:')
    print('1. Ver catálogo')
    print('2. Adicionar ao carrinho')
    print('3. Ver carrinho')
    print('4. Remover')
    print('5. Finalizar')
    print('6. Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        for p in produtos:
            print(f"ID: {p['id']} | {p['nome']} - R$ {p['preço']} | Estoque: {p['estoque']}")

    elif escolha == '2':
        try:
            id_escolhido = int(input('Digite o ID do produto que deseja adicionar: '))
            produto_encontrado = None

            for produto in produtos:
                if produto['id'] == id_escolhido:
                    produto_encontrado = produto
                    break

            if not produto_encontrado:
                print('Produto não encontrado.')
                continue

            if produto_encontrado['estoque'] == 0:
                print('Produto sem estoque.')
                continue

            quantidade = int(input("Quantidade desejada: "))

            if quantidade <= 0:
                print('Quantidade inválida')
                continue

            if quantidade > produto_encontrado['estoque']:
                print('Estoque insuficiente')
                continue

            for item in carrinho:
                if item['id'] == id_escolhido:
                    item['quantidade'] += quantidade
                    break
            
            else:
                carrinho.append({
                    'id': produto_encontrado['id'],
                    'nome': produto_encontrado['nome'],
                    'preço': produto_encontrado['preço'],
                    'quantidade': quantidade 
                })

                produto_encontrado['estoque'] -= quantidade
                print(f'{quantidade} unidade(s) adicionada(s) ao carrinho.')

        except ValueError:
            print("Digite apenas valores válidos.")
    elif escolha == '3':
        if not carrinho:
            print('Seu carrinho está vazio')
        else:
            print('\nSeu carrinho está com os seguintes itens: ')
            print('-'*40)
            total = 0
            for item in carrinho:
                nome = item['nome']
                qtd = item['quantidade']
                preco_unit = item['preço']
                subtotal = qtd * preco_unit
                total += subtotal
                print(f'{nome} | {qtd} un. | R$ {preco_unit:.2f} cada | Subtotal: R$ {subtotal:.2f}')
            print('-' *40)
            print(f'Total da compra: R$ {total:.2f}')
    
    elif escolha == '4':
        if not carrinho:
            print('Carrinho vazio.')
        else:
            try:
                id_remover = int(input('Digite o ID do produto que deseja remover'))
                encontrado = False

                for item in carrinho:
                    if item['id'] == id_remover:
                        encontrado == True
                        print(f'{item['nome']} - {item['quantidade']} no carrinho.')
                        qtd_remover = int(input('Quantidade a remover: '))

                        if qtd_remover <= 0:
                            print('Quantidade inválida.')
                            break
                        elif qtd_remover >= item['quantidade']:
                            carrinho.remove(item)
                            print("Porduto completamnete removido do carrinho.")
                        else:
                            item['quantidade'] -= qtd_remover
                            print(f'{qtd_remover} unidade(s) removida(s).')

                        for p in produtos:
                            if p['id'] == id_remover:
                                p['estoque'] += qtd_remover
                                break

                        break

                    if not encontrado:
                        print('Produto não encontrado no carrinho.')
            except ValueError:
                print('Digite um número válido.')

    elif escolha == '5':
        if not carrinho:
            print('Seu carrinho está vazio.')
        else:
            print('\nResumo da compra:')
            print('-'*40)
            total = 0
            for item in carrinho:
                subtotal = item['preço'] * item['quantidade']
                total += subtotal
                print(f'{item['nome']} | {item['quantidade']} un. | R$ {item['preço':.2f]} | Subtotal: R$ {subtotal:.2f}')
            print('-'*40)
            print(f'Total: R$ {total:.2f}')
            
            confirmar = input('Deseja finalizar a compra? (s/n): ').lower()
            if confirmar == 's':
                carrinho.clear()
                print('Compra finalizada com sucesso!')
            else:
                print('Compra cancelada...')
    elif escolha == '6':       
        print("Encerrando o sistema. Obrigado!")      
        break     

    else:           
        print('Opção inválida. Tente novamente')
        