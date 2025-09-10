#tempo usado para a criação do código: 19:45h
import requests
import time
import palavras
import random
import os
acabar = False
conquistas = [] 
itens = [] #itens em geral
uso = [] #Itens sendo usados
dano_a_mais = 0 #dano de acordo com a arma
defesa = 0 #defesa ganha de acordo com a armadura
arma = ['excalibur', 'sabre de luz', 'espada']
armadura = ['capacete', 'peitoral']

while True:
    sorteado = random.randint(1,20)
    four_digit = random.randint(1000,9999)
    six_digit = random.randint(100000,999999)
    eight_digit = random.randint(10000000, 99999999)
    derrota = 0
    vitoria = 0
    empate = 0
    ataque_basico = 10
    ataque_secundario = 20
    ataque_especial = 33
    menu = False
    next = False
    sangramento = False

    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    caminho=input('Escolha seu caminho: \n[B]em    ' \
    '[R]egras        ' \
    '[I]tens' \
    '\n[M]al    ' \
    '[C]onquistas    ' \
    '[S]air' \
    '\n(Acaso tenha ganhado algum, selecione o outro): ')

    if not caminho.isalpha():
        continue

    caminho=caminho.lower()

    if caminho in ' ' or not caminho[0] in 'bmcrsi':
        continue

    while caminho[0] == 'b':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

        continuar = input('Você escolheu o caminho do bem, deseja continuar? [S]im [N]ão ')

        if not continuar.isalpha():
            print('Faça uma escolha.')
        continuar = continuar.lower()
        if continuar in ' ' or not continuar[0] in 'sn':
            print('Escolha escrevendo ou "S" ou "N"!!')
            continue

        if continuar[0] == 's':
            while True:
                if os.name == "nt":
                    os.system('cls')
                else:
                    os.system('clear')
                print(
                    'Continuaremos para o jogo, serão 3 partes:\n' \
                    '\nFase 1 - Descubra a palavra;' \
                    '\nFase 2 - Adivinhe o número em 10 tentativas;' \
                    '\nFase 3 - Me ganhe em um pedra, papel, tesoura.\n'
                )

                continuar = input('Leitura feita? [S]im [N]ão \n(se não, você irá voltar para o menu inicial): ')

                if not continuar.isalpha():
                    print('Faça uma escolha')
                    continue
                continuar = continuar.lower()
                if not continuar[0] in 'sn':
                    print('Faça uma escolha')
                    continue

                if continuar[0] == 's':
                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')
                    print('Primeiro jogo... COMECE!!')
                    palavra_formada = ''
                    letras_acertadas = ''
                    palavra_secreta = palavras.palavra_aleatoria().lower()
                    
                    while True:

                        letra_user = input('Digite uma letra ou a palavra secreta: ')
                        letra_user = letra_user.lower()

                        if not letra_user == palavra_secreta:
                            if len(letra_user) > 1:
                                if os.name == "nt":
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Se você tentou adivinhar a palavra, tente de novo. Caso contrário, insira somente uma LETRA por vez!!')
                                print(palavra_formada)
                                continue
                            if not letra_user.isalpha():
                                if os.name == "nt":
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Se você tentou adivinhar a palavra, tente de novo. Caso contrário, insira somente uma LETRA por vez!!')
                                print(palavra_formada)
                                continue

                        palavra_formada = ''

                        if letra_user in palavra_secreta:
                            letras_acertadas += letra_user

                        for letra in palavra_secreta:
                            if letra in letras_acertadas:
                                palavra_formada += letra
                            else:
                                palavra_formada +='*'

                        if os.name == "nt":
                            os.system('cls')
                        else:
                            os.system('clear')
                            
                        print(palavra_formada)

                        if letra_user == palavra_secreta or palavra_formada == palavra_secreta:
                            while True:
                                if os.name == "nt":
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Parabéns, você passou para a segunda fase, continue assim!!' \
                                f'\nA palavra secreta era: "{palavra_secreta}"')
                                continuar = input('Pronto? [S]im [N]ão \n(se não, você voltará para o menu): ')
                                if not continuar.isalpha():
                                    continue
                                continuar = continuar.lower()
                                if not continuar[0] in 'sn':
                                    continue
                                if continuar[0] == 's':
                                    proximo = True
                                    break
                                if continuar[0] == 'n':
                                    menu = True
                                    break
                            if menu or proximo:
                                proximo = False
                                break
                        if menu:
                            break
                    if menu:
                        break

                    if acabar:
                        break

                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')

                    print('Vamos continuar para a fase 2... Que comece o segundo jogo!!')

                    tentativa = 0
                    
                    while tentativa <5:

                        numero = input(f'Adivinhe o número de 1 a 20 em 5 tentativas, tentativa {tentativa+1}/5 \
                            \nNúmero de escolha: '                                       
                            )
                        if not numero.isdigit():
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('Escreva somente números!')
                            continue
                        numero = int(numero)
                        
                        if numero > sorteado:
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('Digite um número menor!')
                            tentativa+=1
                        elif numero < sorteado:
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('Digite um número maior!')
                            tentativa+=1
                        else:
                            print('Parabéns')
                            break
                        if tentativa == 5:
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            menu = True
                            break
                    if menu:
                        break
                    
                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')
                    print('Parabéns, você acertou o número! Passaremos para a última fase.')
                    while True:
                        continuar = input('Pronto para a última fase? [S]im [N]ão \n(Se não, irá voltar para o menu): ')
                        if not continuar.isalpha():
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            continue
                        continuar = continuar.lower()
                        if not continuar[0] in 'sn' or ' ' in continuar:
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            continue
                        if continuar[0] == 's':
                            break
                        if continuar[0] == 'n':
                            menu = True
                            break

                    if menu:
                        break
                    
                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')
                    tentativa = 0

                    print('O jogo agora será jankenpon melhor de 3. \n(Escreva ou "Pedra", ou "Papel", ou "Tesoura")')

                    while tentativa <3:
                        opcao = {
                            1: 'pedra',
                            2: 'papel',
                            3: 'tesoura'
                        }
                        escolha = random.randint(1,3)
                        jankenpon = opcao[escolha]

                        player = input(f'prepare-se...3...2...1... Jogue!!: ')
                        if not player.isalpha():
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue
                        if len(player) <5:
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue

                        player = player.lower()

                        if os.name == "nt":
                            os.system('cls')
                        else:
                            os.system('clear')
                        print(f'A máquina jogou: {jankenpon} \nVocê jogou: {player}')

                        if player == jankenpon:
                            print("Empate!")
                            empate +=1
                        elif (
                            (player == "pedra" and jankenpon == "tesoura") or
                            (player == "papel" and jankenpon == "pedra") or
                            (player == "tesoura" and jankenpon == "papel")
                        ):
                            print("Você venceu!")
                            tentativa += 1
                            vitoria += 1
                        else:
                            print("Você perdeu!")
                            tentativa +=1
                            derrota +=1
                        if vitoria==2 or derrota==2:
                            break
                        print(f'\nVitórias: {vitoria} \nDerrotas: {derrota} \nEmpates: {empate}\n')
                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')

                    if derrota > 1:
                        menu = True
                    elif vitoria >1:
                        while True:
                            print('Parabéns, você ganhou o jogo do bem e ganhou uma conquista e um item!! \n(A não ser que já tenha ganhado antes)')
                            
                            item = random.randint(1, 100)
                            if item == 1 and not 'sabre de luz' in conquistas:
                                itens.append('sabre de luz')
                                conquistas.append('sabre de luz')
                            if not 'Jogo "Bem" feito' in conquistas:
                                conquistas.append('Jogo "Bem" feito')
                                                                
                            continuar = input('Continuar? [S]im [N]ão \n(Se não, o jogo acabará / Se sim, o jogo voltará ao menu): ')
                            if not continuar.isalpha():
                                if os.name == "nt":
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                continue
                            if not continuar[0] in 'sn' or ' ' in continuar:
                                if os.name == "nt":
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                continue
                            if continuar[0] == 's':
                                menu = True
                                break
                            if continuar[0] == 'n':
                                while continuar[0] == 'n':
                                    if os.name == "nt":
                                        os.system('cls')
                                    else:
                                        os.system('clear')
                                    continuar = input('Deseja sair mesmo: [S]im [N]ão ')
                                    if not continuar.isalpha():
                                        continue
                                    continuar = continuar.lower()
                                    if ' ' in continuar or not continuar[0] in 'sn':
                                        continue
                                    if continuar[0] == 's':
                                        acabar = True
                                        break
                                    if continuar[0] == 'n':
                                        if os.name == "nt":
                                            os.system('cls')
                                        else:
                                            os.system('clear')
                                        break
                                    
                                if acabar == True:
                                    break

                    break
                
                if continuar[0] == 'n':
                    break
            if acabar or menu:
                break
        if continuar[0] == 'n':
            menu = True
            break
        elif acabar:
            break
    
    while caminho[0] == 'm':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

        continuar = input('Você escolheu o caminho do mal, deseja continuar? [S]im [N]ão ')

        if not continuar.isalpha():
            print('Faça uma escolha.')
        continuar = continuar.lower()
        if continuar in ' ' or not continuar[0] in 'sn':
            print('Escolha escrevendo ou "S" ou "N"!!')
            continue

        if continuar[0] == 's':
            while True:
                if os.name == "nt":
                    os.system('cls')
                else:
                    os.system('clear')
                print(
                    'Continuaremos para o jogo, serão 3 partes:\n' \
                    '\nFase 1 - Digite na Sequência;' \
                    '\nFase 2 - Mini RPG;' \
                    '\nFase 3 - ...\n'
                )

                continuar = input('Leitura feita? [S]im [N]ão \n(se não, você irá voltar para o menu inicial): ')

                if not continuar.isalpha():
                    print('Faça uma escolha')
                    continue
                continuar = continuar.lower()
                if not continuar[0] in 'sn':
                    print('Faça uma escolha')
                    continue

                if continuar[0] == 's':
                    while True:
                        if os.name == "nt":
                            os.system('cls')
                        else:
                            os.system('clear')
                        
                        print('Vamos para o primeiro jogo... Preste bastante atenção.')
                        continuar = input('Pronto? [S]im [N]ão ')

                        if not continuar.isalpha():
                            print('Faça uma escolha')
                            continue
                        continuar = continuar.lower()
                        if not continuar[0] in 'sn':
                            print('Faça uma escolha')
                            continue
                        if continuar[0] == 's':
                            nivel = 0
                            while True:
                                if os.name == "nt":
                                    os.system('cls')
                                else:
                                    os.system('clear')

                                if nivel == 0:
                                    print(four_digit)
                                elif nivel == 1:
                                    four_digit = None
                                    print(six_digit)
                                else:
                                    six_digit = None
                                    print(eight_digit)

                                if nivel ==0:
                                    time.sleep(0.6)
                                elif nivel ==1:
                                    time.sleep(0.8)
                                else:
                                    time.sleep(1)
                                while True:
                                    if os.name == "nt":
                                        os.system('cls')
                                    else:
                                        os.system('clear')

                                    num_user = input('Digite o número correto: ')

                                    if not num_user.isdigit():
                                        print('Digite apenas números!!')
                                        time.sleep(2)
                                        continue
                                    num_user = int(num_user)
                                    if num_user == four_digit or num_user == six_digit:
                                        if os.name == 'nt':
                                            os.system('cls')
                                        else:
                                            os.system('clear')
                                        print('Parabéns, você passou para o próximo nível')
                                        nivel +=1
                                        continuar = input('Pronto? [S]im [N]ão (Se não você voltará ao menu) ')

                                        if not continuar.isalpha():
                                            print('Faça uma escolha.')
                                        continuar = continuar.lower()
                                        if not continuar[0] in 'sn':
                                            print('Faça uma escolha.')
                                        if continuar[0] == 'n':
                                            menu = True
                                            break
                                        break
                                    elif num_user == eight_digit:
                                        while True:
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')

                                            continuar = input('Parabéns, você passou para a próxima fase.' \
                                            '\npronto para continuar? [S]im [N]ão (Se não, você voltará ao menu) ')
                                            if not continuar.isalpha():
                                                print('Faça uma escolha')
                                                continue
                                            continuar = continuar.lower()
                                            if not continuar[0] in 'sn':
                                                print('Faça uma escolha')
                                                continue
                                            if continuar[0] == 's':
                                                next = True
                                                break
                                            else:
                                                menu = True
                                                break
                                        if menu:
                                            break
                                    else:
                                        menu = True
                                        break
                                    if next:
                                        break
                                if menu or next:
                                    break
                        if menu or next:
                            break
                    if next:
                        next = False
                        while True:
                            vida_player = 100
                            vida_monstro = 30
                            vida_boss = 70
                            if os.name == 'nt':
                                os.system('cls')
                            else:
                                os.system('clear')
                            
                            print('Bem vindo a fase 2 do caminho do mal. Segue os dados do player:')
                            print(f'\nitens: {uso}'
                            f'\nvida: {vida_player}')
                            
                            continuar = input('\nPronto para começar? [S]im [N]ão (Se não, você voltará ao menu) ')

                            if not continuar.isalpha():
                                continue
                            continuar = continuar.lower()
                            if not continuar[0] in 'sn':
                                continue
                            while continuar[0] == 's':
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('O player estava entendiado em sua casa, e queria se divertir de alguma forma...')
                                time.sleep(4)
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Depois de um tempo, o player decidiu sair por ai com alguma garota que encontrasse, para talvez ter um clima entre eles.')
                                time.sleep(4)
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Após sair pela vila, achou uma garota que era de seu tipo, e a convidou para passear pelo bosque.')
                                time.sleep(4)
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Ambos estavam curtindo a voltinha que estavam dando, até se aproximarem um pouco mais e...Urrrrrr')
                                time.sleep(4)
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Essa não, um zombie!!!')
                                time.sleep(3)
                                if os.name == 'nt':
                                    os.system('cls')
                                else:
                                    os.system('clear')
                                print('Após esse momento, player se prepara para o combate')
                                time.sleep(3)
                                while True:
                                    monstro_atual = False
                                    if os.name == 'nt':
                                        os.system('cls')
                                    else:
                                        os.system('clear')
                                    continuar = input('Pronto para o combate? [S]im [N]ão (Se não, você voltará para o menu) ')
                                    if not continuar.isalpha():
                                        continue
                                    continuar = continuar.lower()
                                    if not continuar[0] in 'sn':
                                        continue
                                    while continuar[0] == 's':
                                        
                                        if os.name == 'nt':
                                            os.system('cls')
                                        else:
                                            os.system('clear')
                                        
                                        if vida_player <=0:
                                            print('Você perdeu')
                                            time.sleep(2)
                                            menu = True
                                            break

                                        if vida_boss <= 0:
                                            print('O player derrotou os monstros!!')
                                            item = random.randint(1,50)
                                            if item == 1 and not 'espada' in itens:
                                                conquistas.append('espada')
                                                itens.append('espada')
                                            elif item == 2 and not 'excalibur' in itens:
                                                conquistas.append('excalibur')
                                                itens.append('excalibur')
                                            elif item == 3 and not 'capacete' in itens:
                                                conquistas.append('capacete')
                                                itens.append('capacete')
                                            elif item == 4 and not 'peitoral' in itens:
                                                conquistas.append('peitoral')
                                                itens.append('peitoral')
                                            if 'sabre de luz' in conquistas and 'espada' in conquistas and 'excalibur' in conquistas and 'capacete' in conquistas and 'peitoral' in conquistas and not 'Set completo' in conquistas:
                                                conquistas.append('Set completo')
                                            break

                                        dano = 0
                                        dado = random.randint(1,20)
                                        ataque = random.randint(1,3)
                        
                                        if (
                                            (dado == 20 and 'espada' in uso) or 
                                            (dado == 20 and 'excalibur' in uso) or
                                            (dado == 20 and 'sabre de luz' in uso)
                                        ):
                                            dano = 25 + dano_a_mais
                                        else:
                                            dano = dado + dano_a_mais
                                        
                                        print(f'Ataque de player, jogando o dado...')
                                        time.sleep(1.5)
                                        print(dado)
                                        time.sleep(1.5)
                                        print(f'player deu {dano} de dano!')
                                        time.sleep(3)
                                        if sangramento:
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')
                                            print('Player está sangrando (-5)')
                                            vida_player -= 5
                                            print(f'\nPlayer está com {vida_player} de vida')
                                            sangramento = False
                                            time.sleep(3)

                                        if not vida_monstro <=0:
                                            vida_monstro -= dano
                                        elif vida_boss <=0:
                                            continue
                                                
                                        else:
                                            monstro_atual = True
                                            vida_boss -= dano

                                        if os.name == 'nt':
                                            os.system('cls')
                                        else:
                                            os.system('clear')

                                        if monstro_atual:
                                            if vida_boss <=0:
                                                continue
                                            print(f'O Boss está com {vida_boss} de vida')
                                            time.sleep(3)
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')

                                            if ataque == 1:
                                                ataque = ['mordida', ataque_basico]
                                            elif ataque == 2:
                                                ataque = ['soco', ataque_secundario]
                                            elif ataque == 3:
                                                ataque = ['espancada', ataque_especial]
                                            
                                            print(f'Vez do Boss atacar... Boss está usando {ataque[0]} ({ataque[1]} de dano)')
                                            time.sleep(3)
                                            vida_player -= ataque[1]
                                            if ataque[0] == 'mordida':
                                                sangramento = True
                                                vida_player -= 5
                                                print('Player está sangrando (-5)')
                                                time.sleep(3)
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')
                                            print(f'Player está com {vida_player} de vida')
                                            time.sleep(3)
                                                                 
                                        else:
                                            if vida_monstro <=0:
                                                print('Você derrotou o monstro!!')
                                                time.sleep(3)
                                                if os.name == 'nt':
                                                    os.system('cls')
                                                else:
                                                    os.system('clear')
                                                print('Espera!! Tem outro gigante bem ali!!')
                                                if vida_player <85:
                                                    vida_player += 15
                                                time.sleep(3)
                                            else:
                                                print(f'O monstro está com {vida_monstro} de vida')
                                                time.sleep(3)
                                                if os.name == 'nt':
                                                    os.system('cls')
                                                else:
                                                    os.system('clear')
                                                
                                                if ataque ==1:
                                                    ataque = ['mordida', ataque_basico]
                                                else:
                                                    ataque = ['soco', ataque_secundario]

                                                print(f'Vez do monstro atacar... Monstro está usando {ataque[0]} ({ataque[1]} de dano)')
                                                time.sleep(3)
                                                vida_player -= ataque[1]
                                                if ataque[0] == 'mordida':
                                                    sangramento = True
                                                    vida_player -= 5
                                                    print('Player está sangrando (-5)')
                                                if os.name == 'nt':
                                                    os.system('cls')
                                                else:
                                                    os.system('clear')

                                                print(f'Player está com {vida_player} de vida')
                                                time.sleep(3)                                    
                                        
                                    if continuar[0] == 'n' or menu:
                                        menu = True
                                        break

                                    #fase 3

                                if menu:
                                    break
                                        
                            if continuar[0] == 'n' or menu:
                                menu = True
                                break
                                
                if menu:
                    break
                if continuar[0] == 'n':
                    menu = True
                    break
            if menu:
                break
        if continuar[0] == 'n' or menu:
            break
    while caminho[0] == 'r':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print('Para deixar mais claro, esse jogo possui algumas regras e explicações:\n' \
        '\n1 - Acaso perder algum desafio, o jogo te trará para o menu.' \
        '\n2 - O nível do bem é mais fácil do que o nível do mal, \napesar disso, você dependerá MUITO da sua sorte para passar.' \
        '\n3 - A primeira fase do nível do bem está usando palavras em \ninglês.' \
        '\n4 - É possível "Platinar" o jogo.')
        voltar = input('\nDigite "V" para voltar: ')
        if not voltar.isalpha():
            continue
        voltar = voltar.lower()
        if not voltar[0] in 'v':
            continue
        else:
            break
    while caminho[0] == 'c':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print(f'Bem vindo a aba de conquistas, atualmente você possui {len(conquistas)}.')
        print(conquistas)
        voltar = input('Digite "V" para voltar: ')
        if not voltar.isalpha():
            continue
        voltar = voltar.lower()
        if not voltar[0] in 'v':
            continue
        else:
            break
    while caminho[0] == 's':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        continuar = input('Deseja sair mesmo? [S]im [N]ão ')
        if not continuar.isalpha():
            continue
        continuar = continuar.lower()
        if ' ' in continuar or not continuar[0] in 'sn':
            continue
        if continuar[0] == 's':
            if os.name == "nt":
                os.system('cls')
            else:
                os.system('clear')
            acabar = True
            break
        if continuar[0] == 'n':
            break
    while caminho[0] == 'i':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print(f'Bem vindo a aba de itens, atualmente você possui {len(itens)}.')
        print(itens)
        equipar = input('Deseja equipar algum item?' \
        '\n(Se sim, escrever o nome do item, se não, digite "não") ')
        if not equipar.isalpha():
            continue
        equipar = equipar.lower()
        if equipar in uso:
            print('Item já está em uso')
            time.sleep(3)
            continue
        elif not equipar in itens:
            print('Você não tem este item para poder usa-lo')
            time.sleep(3)
            continue
        elif equipar in armadura:
            if uso:
                uso.remove(uso[0])
            uso.append(equipar)
        elif equipar in arma:
            if uso:
                uso.remove(uso[0])
            uso.append(equipar)
        elif equipar[0] == 'n':
            ...
        else:
            continue
        print(f'Item em uso: {uso}')
        voltar = input('Digite "V" para voltar: ')
        if not voltar.isalpha():
            continue
        voltar = voltar.lower()
        if not voltar[0] in 'v':
            continue
        else:
            break
    if acabar:
        break
