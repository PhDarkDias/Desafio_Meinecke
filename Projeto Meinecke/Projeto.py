
class Loja:
    def __init__(self):
        self.nome = input("Nome da loja: ")
        self.endereco = input("Endereço da loja: ")
        self.contato = self.validar_contato(input("Contato da loja: "))
        self.email = self.validar_email(input("E-mail da loja: "))
        self.estoque = {}

    def validar_contato(self, contato):
        while True:
            contato_limpo = ''.join(filter(str.isdigit, contato))
            if len(contato_limpo) == 11 and contato_limpo[2] == '9':
                return f"({contato_limpo[:2]}) 9 {contato_limpo[3:7]}-{contato_limpo[7:]}"
            elif len(contato_limpo) == 10:
                return f"({contato_limpo[:2]}) {contato_limpo[2:6]}-{contato_limpo[6:]}"
            else:
                print("Formato de contato inválido. O formato correto é (DD) 9 0000-0000 ou (DD) 0000-0000.")
                contato = input("Contato da loja: ")

    def validar_email(self, email):
        while not email.endswith("@gmail.com"):
            print("Formato de e-mail inválido. O e-mail deve terminar com '@gmail.com'.")
            email = input("E-mail da loja: ")
        return email

    def adicionar_produto(self, produto, quantidade, fornecedor=None):
        if produto in self.estoque:
            self.estoque[produto]['quantidade'] += quantidade
        else:
            self.estoque[produto] = {'quantidade': quantidade, 'fornecedor': fornecedor}

    def diminuir_quantidade_produto(self, produto, quantidade):
        if produto in self.estoque:
            estoque_atual = self.estoque[produto]['quantidade']
            if estoque_atual >= quantidade:
                self.estoque[produto]['quantidade'] -= quantidade
                print(f"{quantidade} unidades do produto {produto} removidas do estoque.")
            else:
                print(f"Quantidade insuficiente de {produto} em estoque.")
        else:
            print(f"{produto} não encontrado em estoque.")

    def exibir_dados_loja(self):
        print("Dados da loja:")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Contato: {self.contato}")
        print(f"E-mail: {self.email}")

    def exibir_estoque(self):
        print("Estoque da loja:")
        for produto, info in self.estoque.items():
            quantidade = info['quantidade']
            fornecedor = info['fornecedor']
            print(f"{produto}: {quantidade} (Fornecedor: {fornecedor})")

# ============================================================================================
# ============================================================================================

class Fornecedor:
    def __init__(self):
        self.nome = input("Nome do fornecedor: ")
        self.endereco = input("Endereço do fornecedor: ")
        self.contato = self.validar_contato(input("Contato do fornecedor: "))
        self.email = self.validar_email(input("E-mail do fornecedor: "))
        self.produtos_fornecidos = {}

    def validar_contato(self, contato):
        while True:
            # Remover espaços em branco e caracteres não numéricos
            contato_limpo = ''.join(filter(str.isdigit, contato))
            # Verificar se o formato é válido ((DDD) 9 0000-0000)
            if len(contato_limpo) == 11 and contato_limpo[2] == '9':
                return f"({contato_limpo[:2]}) 9 {contato_limpo[3:7]}-{contato_limpo[7:]}"
            elif len(contato_limpo) == 10:
                return f"({contato_limpo[:2]}) {contato_limpo[2:6]}-{contato_limpo[6:]}"
            else:
                print("Formato de contato inválido. O formato correto é (DD) 9 0000-0000 ou (DD) 0000-0000.")
                contato = input("Contato do fornecedor: ")

    def validar_email(self, email):
        while not email.endswith("@gmail.com"):
            print("Formato de e-mail inválido. O e-mail deve terminar com '@gmail.com'.")
            email = input("E-mail do fornecedor: ")
        return email

    def exibir_dados_fornecedor(self):
        print("Dados do fornecedor:")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Contato: {self.contato}")
        print(f"E-mail: {self.email}")
        print("Produtos fornecidos:")
        for produto, quantidade in self.produtos_fornecidos.items():
            print(f"- {produto}: {quantidade}")

    def adicionar_produto_fornecido(self):
        produto = input("Nome do produto fornecido: ")
        quantidade = int(input("Quantidade fornecida: "))
        self.produtos_fornecidos[produto] = quantidade

    def fornecer_produtos_para_loja(self, loja):
        for produto, quantidade in self.produtos_fornecidos.items():
            loja.adicionar_produto(produto, quantidade, self.nome)

# ============================================================================================
# ============================================================================================

minha_loja = None
fornecedores = []

def cadastrar_loja():
    return Loja()

def ver_informacoes_loja(loja):
    loja.exibir_dados_loja()

def cadastrar_fornecedores():
    fornecedores = []
    while True:
        novo_fornecedor = Fornecedor()
        while True:
            novo_fornecedor.adicionar_produto_fornecido()
            continua = input("Deseja adicionar outro produto para este fornecedor? (s/n): ")
            if continua.lower() != 's':
                break
        fornecedores.append(novo_fornecedor)
        for fornecedor in fornecedores:
            fornecedor.fornecer_produtos_para_loja(minha_loja)
        continua = input("Deseja adicionar outro fornecedor? (s/n): ")
        if continua.lower() != 's':
            break
    return fornecedores

def ver_informacoes_fornecedores(fornecedores):
    print("Dados de todos os fornecedores:")
    for fornecedor in fornecedores:
        fornecedor.exibir_dados_fornecedor()

def ver_estoque_loja(loja):
    loja.exibir_estoque()

def diminuir_quantidade_produto_loja(loja):
    produto = input("Digite o nome do produto a ser removido do estoque: ")
    quantidade = int(input("Digite a quantidade a ser removida do estoque: "))
    loja.diminuir_quantidade_produto(produto, quantidade)

def menu():
    print("Menu:")
    print("1. Cadastrar loja")
    print("2. Ver informações da loja")
    print("3. Cadastrar fornecedores")
    print("4. Ver informações dos fornecedores")
    print("5. Ver estoque da loja")
    print("6. Remover quantidade de produto do estoque")
    print("7. Sair")


while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        minha_loja = cadastrar_loja()
    elif opcao == '2':
        if minha_loja:
            ver_informacoes_loja(minha_loja)
        else:
            print("Loja ainda não cadastrada.")
    elif opcao == '3':
        fornecedores += cadastrar_fornecedores()
    elif opcao == '4':
        if fornecedores:
            ver_informacoes_fornecedores(fornecedores)
        else:
            print("Nenhum fornecedor cadastrado.")
    elif opcao == '5':
        if minha_loja:
            ver_estoque_loja(minha_loja)
        else:
            print("Loja ainda não cadastrada.")
    elif opcao == '6':
        if minha_loja:
            ver_estoque_loja(minha_loja)
            diminuir_quantidade_produto_loja(minha_loja)
        else:
            print("Loja ainda não cadastrada.")

    elif opcao == '7':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
