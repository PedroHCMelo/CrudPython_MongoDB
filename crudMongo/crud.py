
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://pedrohcm:<teste>@cluster0.cjhzt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
contacts_collection = db["contacts"]

# Função para cadastrar um novo contato
def cadastrar_contato(nome, telefone):
    contato = {
        "nome": nome,
        "telefone": telefone
    }
    result = contacts_collection.insert_one(contato)
    print(f"Contato {nome} inserido com o ID: {result.inserted_id}")

# Função para listar todos os contatos
def listar_contatos():
    contatos = contacts_collection.find()
    print("Lista de contatos:")
    for contato in contatos:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

# Função para buscar contato por nome
def buscar_contato_por_nome(nome):
    contato = contacts_collection.find_one({"nome": nome})
    if contato:
        print(f"Contato encontrado - Nome: {contato['nome']}, Telefone: {contato['telefone']}")
    else:
        print(f"Contato com nome {nome} não encontrado.")

# Função para excluir um contato
def excluir_contato(nome):
    result = contacts_collection.delete_one({"nome": nome})
    if result.deleted_count > 0:
        print(f"Contato {nome} excluído com sucesso.")
    else:
        print(f"Contato {nome} não encontrado.")

# Menu de opções
def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar contato")
        print("2. Listar contatos")
        print("3. Buscar contato por nome")
        print("4. Excluir contato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            cadastrar_contato(nome, telefone)
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            nome = input("Digite o nome do contato que deseja buscar: ")
            buscar_contato_por_nome(nome)
        elif opcao == "4":
            nome = input("Digite o nome do contato que deseja excluir: ")
            excluir_contato(nome)
        elif opcao == "5":
            print("Saindo do aplicativo.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
