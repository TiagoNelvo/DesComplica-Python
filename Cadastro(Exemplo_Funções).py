def cadastrar(pessoas):
    cpf = input("Digite seu cpf: ")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    pessoas.append((cpf, nome, idade))
    
    
def listar(pessoas):
    for pessoa in pessoas:
        cpf, nome, idade = pessoa
        print(f'Nome {nome} e sua idade {idade} com o cpf: {cpf} ')
        
def exibir_menu():
    print(''' \n Escolha uma opção: 
    1. Cadastrar Pessoa
    2. Listar Pessoa
    3. Sair''')
    
def main():
    pessoas = []
    flag = True
    while flag:
        exibir_menu()
        try:
            opcao = int(input("Digite a opção: "))
            if opcao == 1:
                cadastrar(pessoas)
            elif opcao == 2:
                listar(pessoas)
            elif opcao == 3:
                flag = False
            else:
                print("Opção invalida")
        except ValueError:
            print("Favor digitar somente números")


main()