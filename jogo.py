import requests

url = "https://random-word-api.herokuapp.com/word?number=1"

import random
import os
acabar = False
conquistas = []

while True:
    sorteado = random.randint(1,20)
    resposta = requests.get(url)
    derrota = 0
    vitoria = 0
    empate = 0
    menu = False
    os.system('clear')
    caminho=input('Escolha seu caminho: \n[B]em    ' \
    '[R]egras' \
    '\n[M]al    ' \
    '[C]onquistas    ' \
    '[S]air' \
    '\n(Acaso tenha ganhado algum, selecione o outro): ')

    if not caminho.isalpha():
        continue

    caminho=caminho.lower()

    if caminho in ' ' or not caminho[0] in 'bmcrs':
        continue

    while caminho[0] == 'b':
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
                    os.system('clear')
                    print('Primeiro jogo... COMECE!!')
                    palavra_formada = ''
                    letras_acertadas = ''

                    while True:

                        if resposta.status_code == 200:
                            palavra = resposta.json()[0]
                        else:
                            print("Erro ao acessar a API. Código:", resposta.status_code)
                        palavra_secreta = palavra

                        letra_user = input('Digite uma letra ou a palavra secreta: ')
                        letra_user = letra_user.lower()

                        if not letra_user == palavra_secreta:
                            if len(letra_user) > 1:
                                os.system('clear')
                                print('Se você tentou adivinhar a palavra, tente de novo. Caso contrário, insira somente uma LETRA por vez!!')
                                print(palavra_formada)
                                continue
                            if not letra_user.isalpha():
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

                        os.system('clear')
                            
                        print(palavra_formada)

                        if letra_user == palavra_secreta or palavra_formada == palavra_secreta:
                            while True:
                                os.system('clear')
                                print('Parabéns, você passou para a segunda fase, continue assim!!')
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

                    os.system('clear')

                    print('Vamos continuar para a fase 2... Que comece o segundo jogo!!')

                    tentativa = 0
                    
                    while tentativa <5:

                        numero = input(f'Adivinhe o número de 1 a 20 em 5 tentativas, tentativa {tentativa+1}/5 \
                            \nNúmero de escolha: '                                       
                            )
                        if not numero.isdigit():
                            os.system('clear')
                            print('Escreva somente números!')
                            continue
                        numero = int(numero)
                        
                        if numero > sorteado:
                            os.system('clear')
                            print('Digite um número menor!')
                            tentativa+=1
                        elif numero < sorteado:
                            os.system('clear')
                            print('Digite um número maior!')
                            tentativa+=1
                        else:
                            print('Parabéns')
                            break
                        if tentativa == 5:
                            os.system('clear')
                            print('Game over!!')
                            menu = True
                            break
                    if menu:
                        break
                    
                    os.system('clear')
                    print('Parabéns, você acertou o número! Passaremos para a última fase.')
                    while True:
                        continuar = input('Pronto para a última fase? [S]im [N]ão \n(Se não, irá voltar para o menu): ')
                        if not continuar.isalpha():
                            os.system('clear')
                            continue
                        continuar = continuar.lower()
                        if not continuar[0] in 'sn' or ' ' in continuar:
                            os.system('clear')
                            continue
                        if continuar[0] == 's':
                            break
                        if continuar[0] == 'n':
                            menu = True
                            break

                    if menu:
                        break
                    
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
                            os.system('clear')
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue
                        if len(player) <5:
                            os.system('clear')
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue

                        player = player.lower()

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
                    os.system('clear')

                    if derrota > 1:
                        print('Game Over!!')
                        menu = True
                    elif vitoria >1:
                        while True:
                            print('Parabéns, você ganhou o jogo do "bem" e ganhou uma conquista!! \
                                \nVeja sua conquista na opção "Conquistas"')
                            
                            conquistas.append('Jogo "Bem" feito.')
                            continuar = input('Continuar? [S]im [N]ão \n(Se não, o jogo acabará / Se sim, o jogo voltará ao menu): ')
                            if not continuar.isalpha():
                                os.system('clear')
                                continue
                            if not continuar[0] in 'sn' or ' ' in continuar:
                                os.system('clear')
                                continue
                            if continuar[0] == 's':
                                menu = True
                                break
                            if continuar[0] == 'n':
                                while continuar[0] == 'n':
                                    os.system('clear')
                                    continuar = input('Deseja sair mesmo: [S]im [N]ão ')
                                    if not continuar.isalpha():
                                        continue
                                    continuar = continuar.lower()
                                    if ' ' in continuar or not continuar[0] in 'sn':
                                        continue
                                    if continuar[0] == 'n':
                                        break
                                    
                                acabar = True
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
        ...
    while caminho[0] == 'r':
        os.system('clear')
        print('Para deixar mais claro, esse jogo possui algumas regras e explicações:\n' \
        '\n1 - Acaso perder em qualquer jogo, é game over!\nSeu processo não será salvo, incluindo as conquistas, e o código acabará.' \
        '\n2 - O nível do bem é mais fácil do que o nível do mal, \napesar disso, você dependerá da sua sorte para passar')
        voltar = input('\nDigite "V" para voltar: ')
        if not voltar.isalpha():
            continue
        voltar = voltar.lower()
        if not voltar[0] in 'v':
            continue
        else:
            break
    while caminho[0] == 'c':
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
            break
    if acabar:
        break
