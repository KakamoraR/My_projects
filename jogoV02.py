import random, time, os, palavras, sys

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    while True:
        limpar()
        caminhos = input('1)Bem \t2)Regras \t3)Itens \n4)Mal \t5)Conquistas \t6)Sair\n')
        if caminhos not in '123456' or not caminhos:
            continue
        return caminhos[0]

def continuar():
    while True:
        limpar()
        continuar = input('Deseja continuar? \n1)Sim \t2)Não\n')
        if continuar not in '12':
            continue
        if continuar[0] == '2':
            return False
        return
    
def modo():
    while True:
        limpar()
        modo = input('Selecione um modo (mudável nas regras): \n1)Speedrun \t2)História\n')
        if modo not in '12' or not modo:
            continue
        return modo[0]

def caminho_bem():

    while True:
        if continuar() == False:
            break

        limpar()

        print('Vamos para a primeira fase do caminho do bem, adivinhe a palavra!!!')
        time.sleep(2 if modo == '2' else 0)

        palavra_secreta = palavras.palavra_aleatoria().lower()
        letras_certas = ''

        limpar()

        while True:
            palavra_formada = ''
            resposta_usuario = input('Digite uma letra ou uma palavra: ')

            if not resposta_usuario.isalpha():
                continue

            if resposta_usuario.lower() == palavra_secreta:
                break

            if resposta_usuario.lower() in palavra_secreta and not resposta_usuario.lower() in letras_certas:
                letras_certas += resposta_usuario.lower()

            for letra in palavra_secreta:
                if letra in letras_certas:
                    palavra_formada += letra
                else:
                    palavra_formada += '*' 
            
            limpar()

            if palavra_formada == palavra_secreta:
                print('Parabéns, você passou para a próxima fase.')
                time.sleep(2 if modo == '2' else 0)
                break

            print(palavra_formada)
        
        if continuar() == False:
            break

        limpar()

        print('Vamos para a segunda fase do caminho do bem, adivinhe o número de 1 a 20 em 5 tentativas!!!')
        time.sleep(2 if modo == '2' else 0)

        limpar()

        numero_sortido = random.randint(1,20)
        tentativa = 0

        while tentativa < 5:

            numero_usuario = input(f'Escolha um número de 1 a 20 (tentativa {tentativa+1}/5)\n')

            limpar()

            if not numero_usuario.isdigit():
                limpar()
                continue

            tentativa += 1
            
            if int(numero_usuario) == numero_sortido:
                print('Parabéns, você passou para a próxima fase.')
                time.sleep(2 if modo == '2' else 0)
                break
            elif int(numero_usuario) > numero_sortido:
                print('Escolha um número menor')
                continue
            elif int(numero_usuario) < numero_sortido:
                print('Escolha um número maior')
                continue
        
        if tentativa = 5 or continuar() == False:
            break

        ... #Terceira fase

def caminho_mal():
    ...

def conquistas():
    ...

def regras():
    ...

def sair():
    limpar()
    sys.exit()

def itens():
    ...

modo = modo() #colocar nas regras para escolha mid game

while True:

    caminho = menu()

    if caminho == '1':
        caminho_bem()
    elif caminho == '2':
        regras()
    elif caminho == '3':
        itens()
    elif caminho == '4':
        caminho_mal()
    elif caminho == '5':
        conquistas()
    elif caminho == '6':
        sair()
