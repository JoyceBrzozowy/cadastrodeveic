#Lista para armazenar os veículos
class Veiculo:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

def cadastrar_veiculo():
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    ano = input("Digite o ano do veículo: ")

    veiculo = Veiculo(modelo, cor, ano)
    return veiculo

def listar_veiculos(veiculos):
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    else:
        print("Lista de veículos cadastrados:")
        for i, veiculo in enumerate(veiculos, 1):
            print(f"{i}. Modelo: {veiculo.modelo}, Cor: {veiculo.cor}, Ano: {veiculo.ano}")

def main():
    veiculos = []

    while True:
        print("\n*** Sistema de Cadastro de Veículos ***")
        print("1. Cadastrar Veículo")
        print("2. Listar Veículos Cadastrados")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_veiculo = cadastrar_veiculo()
            veiculos.append(novo_veiculo)
            print("Veículo cadastrado com sucesso!")

        elif opcao == "2":
            listar_veiculos(veiculos)

        elif opcao == "3":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

#Considerando um bd, utilizando pyodbc para conex


import pyodbc

class Veiculo:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

def conectar_banco():
    try:
        conexao = pyodbc.connect('DRIVER={SQL Server};'
                                 'SERVER=seu_servidor;'
                                 'DATABASE=seu_banco_de_dados;'
                                 'UID=seu_usuario;'
                                 'PWD=sua_senha')
        return conexao
    except pyodbc.Error as ex:
        print(f"Erro na conexão com o banco de dados: {ex}")
        return None

def criar_tabela_veiculos(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Veiculos (
                ID INT IDENTITY(1,1) PRIMARY KEY,
                Modelo NVARCHAR(255),
                Cor NVARCHAR(255),
                Ano INT
            )
        ''')
        conexao.commit()
    except pyodbc.Error as ex:
        print(f"Erro ao criar a tabela: {ex}")

def cadastrar_veiculo(conexao):
    modelo = input("Digite o modelo do veículo: ")
    cor = input("Digite a cor do veículo: ")
    ano = input("Digite o ano do veículo: ")

    try:
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO Veiculos (Modelo, Cor, Ano) VALUES (?, ?, ?)', modelo, cor, ano)
        conexao.commit()
        print("Veículo cadastrado com sucesso!")
    except pyodbc.Error as ex:
        print(f"Erro ao cadastrar veículo: {ex}")

def listar_veiculos(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT Modelo, Cor, Ano FROM Veiculos')
        veiculos = cursor.fetchall()

        if not veiculos:
            print("Nenhum veículo cadastrado.")
        else:
            print("Lista de veículos cadastrados:")
            for veiculo in veiculos:
                print(f"Modelo: {veiculo.Modelo}, Cor: {veiculo.Cor}, Ano: {veiculo.Ano}")
    except pyodbc.Error as ex:
        print(f"Erro ao listar veículos: {ex}")

def main():
    conexao = conectar_banco()

    if conexao:
        criar_tabela_veiculos(conexao)

        while True:
            print("\n*** Sistema de Cadastro de Veículos ***")
            print("1. Cadastrar Veículo")
            print("2. Listar Veículos Cadastrados")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_veiculo(conexao)

            elif opcao == "2":
                listar_veiculos(conexao)

            elif opcao == "3":
                print("Saindo do sistema. Até mais!")
                break

            else:
                print("Opção inválida. Tente novamente.")

        conexao.close()

if __name__ == "__main__":
    main()


# Não esquecer de mudar os valores (servidor, nome bd, usuario, senha)
# Ver depois
    

