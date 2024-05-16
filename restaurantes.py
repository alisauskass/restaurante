import time
import os

def gravar_cadastro(cadastro, endereco):
    with open('restaurantes.txt', 'a') as arquivo:
        arquivo.write(f"{cadastro};{endereco}\n")

def listar_restaurantes():
    with open('restaurantes.txt', 'r') as arquivo:
        restaurantes = arquivo.readlines()
    for restaurante in restaurantes:
        cadastro, endereco = restaurante.strip().split(';')
        print(f"- {cadastro}: {endereco}")

while True:
    intervalo = 1

    print("cadastreirogourmet.com.br")
    print("\n - SEJA BEM-VINDO AO NOSSO SITE DE CADASTRO DE RESTAURANTES DE OSASCO -")
    time.sleep(2)
    print("""𝘾𝘼𝘿𝘼𝙎𝙏𝙍𝙊 𝙊𝙎𝘼𝙎𝘾𝙊""")
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
    opcao = input("\nEscolha uma opção:")
    if (int(opcao) not in (1, 2, 3, 4)):
        os.system('cls')
        print ("Opção Inválida")
        continue
    if (int(opcao) == 1): #cadastrar
        os.system('cls')
        print("\nSeja bem-vindo à tela de cadastro de restaurantes de Osasco")
        time.sleep(intervalo)
        proprietario = input("Qual o nome do proprietário?: ")
        print("\nOlá", proprietario,", vamos começar o cadastro do seu restaurante")
        time.sleep(1)
        cadastro = input("Escolha o nome do seu restaurante: ")
        endereco = input("Qual o endereço do seu comércio?: ")
        print("\nRestaurante cadastro com sucesso")
        print("\nO nome do seu restaurante é", cadastro)
        print("E está localizado no endereço", endereco)
        print("Nome do proprietário: ", proprietario)
        time.sleep(1)
        print("\nRESTAURANTE CADASTRADO!\nVocê será redirecionado ao início do site.")
        gravar_cadastro(cadastro, endereco)
        time.sleep(2)
        continue
    elif (int(opcao) == 2): #listarq
        print("Olá! Nós vamos listar os restaurantes registrados em Osasco\nno dia de hoje")
        listar_restaurantes()
        voltar = input("Pressione 'ENTER' para voltar à página inicial!")
        if voltar.lower() == '':
            print("Retornando à tela inicial...")
            time.sleep(3)
            os.system('cls')
            continue
    elif (int(opcao) == 3): #ativar
        os.system('cls')
        ativa = input("Qual o nome do restaurante que você deseja ativar?: ")
        with open('restaurantes.txt', 'r') as arquivo:
            restaurantes = arquivo.readlines()
        if any(ativa in restaurante for restaurante in restaurantes):
            print("\nNós achamos o seu restaurante em nosso sistema!\no seu restaurante está cadastrado novamente.")
            print(f"Muito obrigado, dono da '{ativa}'")
        else:
            print("Desculpe, não encontramos o restaurante desejado.")
        time.sleep(3)
        os.system('cls')
        continue
    elif (int(opcao) == 4): #sair
        os.system('cls')
        print("Muito obrigado pela sua visita!\n\nAté a próxima\n")
        print("Site fechado.")
        time.sleep(3)
        os.system('cls')
        break