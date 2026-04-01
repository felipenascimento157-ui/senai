# cria a variavel nome 
nome = input("Digite seu nome: ")

print(f"Bem Vindo, {nome}")
#usado para aparecer a informação na tela 

while True:#cria um laço de repetição


    user = float(input("Qual tipo de usuário você é?\n1- Membro\n2- VIsitantes\n3- Saír\n\nQual opção você deseja?: "))
    #escolher a opção que você quer 

    if user == 2:
        time = float(input("Digite a quantidade de horas que você deseja ficar logado(a) (maximo 4): "))
        if time <= 4:
            print(f"Olá, {nome}, seu login foi feito com sucesso!")
            break
#se  o  horario for maior que 4
        if time > 4:
            print("Acesso negado! Quantidade de horas inválida.\n")
            tentativa = input("Tentar novamente?\n1- Sim\n2- Não\n\nEscolha: ")
            if tentativa == 1:
                continue
            elif tentativa == 2:
                print("Saíndo...")
                break
    if user == 1:
        print("Bem Vindo!, tempo de login: 9h da manha, até as 18h da tarde")
        break

    if user == 3:
        print("Até a proxima!")
        break
