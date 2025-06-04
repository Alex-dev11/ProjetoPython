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
while True:
    print('\nMENU:')
    print('1. Ver catálogo')
    print('2. Adicionar ao carrinho')
    print('3. Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        for p in produtos:
            print(f"ID: {p['id']} | {p['nome']} - R$ {p['preço']} | Estoque: {p['estoque']}")
