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
    print(cor("\n📦 CATÁLOGO DE PRODUTOS\n", "1;34"))
    print(cor(f"{'ID':<4}{'Produto':<40}{'Preço':<12}{'Estoque':<8}", "1;37"))
    for p in produtos:
         print(f"{p['id']:<4}{p['nome']:<40}R$ {p['preço']:<10.2f}{p['estoque']:<8}")

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
            print(cor('Produto não encontrado.❌', "1;31"))
            return

        if produto['estoque'] == 0:
                print(cor('Produto sem estoque.', "1;33"))
                return

        quantidade = int(input("Quantidade desejada: "))
        
        if quantidade <= 0:
            print(cor('Quantidade inválida. ❌', "1;31"))
            return

        if quantidade > produto['estoque']:
            print(cor('Estoque insuficiente. ❌', "1;31"))
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
        print(cor(f'{quantidade} unidade(s) adicionada(s) ao carrinho. ✅', "1;32"))

    except ValueError:
        print(cor("Digite apenas valores válidos.","1;31"))

def ver_carrinho():
    print(cor("\n🧺 SEU CARRINHO:\n", "1;36"))
    if not carrinho:
        print(cor('Seu carrinho está vazio', "1;31"))
        return
    print(cor(f"{'Produto':<40}{'Qtd':<6}{'Subtotal':<10}", "1;37"))
    total = 0
    for item in carrinho:
        subtotal = item['quantidade'] * item['preço']
        total += subtotal
        print(f"{item['nome']:<40}{item['quantidade']:<6}R$ {subtotal:.2f}")
    print(cor(f"\n🧾 Total: R$ {total:.2f}", "1;32"))

def remover_do_carrinho():
    try:
        id_remover = int(input('Digite o ID do produto que deseja remover: '))

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
                print(cor("Item removido com sucesso. 🗑️", "1;32"))
                return
        print(cor('Item não encontrado no carrinho.', "1;31"))
    except ValueError:
        print(cor('Entrada inválida.', "1;31"))
                           
def finalizar_compra():
    if not carrinho:
        print(cor("\nSeu carrinho está vazio. Nada a finalizar.", "1;33"))
        return
    print(cor("\n🧾 RESUMO DA COMPRA", "1;34"))
    total = 0
    for item in carrinho:
        subtotal = item['quantidade'] * item['preço']
        total += subtotal
        print(f"{item['nome']:<40}{item['quantidade']} un. | R$ {subtotal:.2f}")
    print(cor("-" * 60, "1;37"))
    print(cor(f"TOTAL FINAL: R$ {total:.2f}", "1;32"))
    carrinho.clear()
    print(cor(" Compra finalizada com sucesso! ✅", "1;32"))
           
while True:
    exibir_menu()
    escolha = input(cor('Escolha uma opção: ', "1;36"))
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
         print(cor('Encerrando programa...' , "1;35"))
         break
    else:
         print(cor('Opção inválida. Tente novamente', "1;31"))