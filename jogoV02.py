import random, time, os, palavras, sys

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def tempo():
    global modo
    time.sleep(2.5 if modo == '2' else 0)

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
        tempo()

        palavra_secreta = palavras.palavra_aleatoria().lower()
        letras_certas = ''
        palavra_formada = ''

        limpar()

        while True:
            resposta_usuario = input('Digite uma letra ou uma palavra: ')

            if not resposta_usuario.isalpha():
                limpar()
                print(palavra_formada if palavra_formada else 'Digite uma letra ou a palavra secreta')
                continue

            palavra_formada = ''

            if resposta_usuario.lower() == palavra_secreta:
                break

            if resposta_usuario.lower() in palavra_secreta:
                letras_certas += resposta_usuario.lower()

            for letra in palavra_secreta:
                if letra in letras_certas:
                    palavra_formada += letra
                else:
                    palavra_formada += '*' 
            
            limpar()

            if palavra_formada == palavra_secreta:
                print('Parabéns, você passou para a próxima fase.')
                tempo()
                break

            print(palavra_formada)
        
        if continuar() == False:
            break

        limpar()

        print('Vamos para a segunda fase do caminho do bem, adivinhe o número de 1 a 20 em 5 tentativas!!!')
        tempo()

        limpar()

        numero_sortido = random.randint(1,20)
        tentativa = 0
        numero_anterior = 0

        while tentativa < 5:

            numero_usuario = input(f'Escolha um número de 1 a 20 (tentativa {tentativa+1}/5)\n')

            limpar()

            if not numero_usuario.isdigit():
                limpar()
                if numero_anterior == 0:
                    print('Escolha entre 1 e 20!!')
                elif numero_anterior > numero_sortido:
                    print(f'Escolha um número menor que {numero_anterior}')
                elif numero_anterior < numero_sortido:
                    print(f'Escolha um número maior que {numero_anterior}')
                continue
            
            if int(numero_usuario) == numero_sortido:
                print('Parabéns, você passou para a próxima fase.')
                tempo()
                break
            elif int(numero_usuario) > numero_sortido:
                print(f'Escolha um número menor que {numero_usuario}')
                numero_anterior = int(numero_usuario)
                tentativa += 1
                continue
            elif int(numero_usuario) < numero_sortido:
                print(f'Escolha um número maior que {numero_usuario}')
                numero_anterior = int(numero_usuario)
                tentativa += 1
                continue
        
        if tentativa == 5:
            limpar()
            print('Infelizmente você perdeu')
            time.sleep(2)
            break
        elif continuar() == False:
            break

        limpar()

        print('Vamos para a terceira fase do caminho do bem, ganhe um janknepon melhor de 3!!!')

        limpar()

        empates = 0
        vitorias = 0
        derrotas = 0

        while True:

            computador = random.randint(1, 3)

            player = input('Escolha entre: \n1)Pedra \t2)papel \t3)Tesoura\n')

            limpar()

            if not player.isdigit():
                continue

            if str(computador) == player:
                print('Vocês empataram')
                empates += 1
            elif (str(computador) == '1' and player == '2') or \
            (str(computador) == '2' and player == '3') or \
            (str(computador) == '3' and player == '1'):
                print('Você venceu')
                vitorias += 1
            else:
                print('Você perdeu')
                derrotas += 1

            if derrotas == 2 or vitorias == 2:
                break

            print(f'Derrotas: {derrotas} \nVitórias: {vitorias} \nEmpates: {empates}')

        limpar()

        if derrotas == 2:
            print('Infelizmente você perdeu')
        else:
            print('Parabéns, você zerou o Caminho do Bem')
        time.sleep(2)
        break

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
