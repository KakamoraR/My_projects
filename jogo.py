import random
import os
acabar = False
conquistas = []

while True:
    sorteado = random.randint(1,20)
    derrota = 0
    vitoria = 0
    empate = 0
    menu = False
    os.system('clear')
    caminho=input('Escolha seu caminho: [B]em ou [M]al \n(Acaso tenha ganhado algum, selecione o outro): ')

    if len(caminho) > 1 or not caminho.isalpha():
        print('Escolha o caminho somente digitando "B" ou "M"')

    caminho=caminho.lower()

    if not caminho in 'bm':
        print('Escolha o caminho somente digitando "B" ou "M"')

    while caminho == 'b':
        os.system('clear')

        if caminho == 'b':
            continuar = input('Você escolheu o caminho do bem, deseja continuar? [S]im [N]ão ')

            if len(continuar) >1:
                print('escreva somente uma letra!!')
                continue
            continuar = continuar.lower()
            if not continuar in 'sn' or continuar in ' ':
                print('Escolha escrevendo ou "S" ou "N"!!')
                continue

            if continuar == 's':
                while True:
                    os.system('clear')
                    print(
                        'Continuaremos para o jogo, serão 3 partes:\n' \
                        '\nFase 1 - Descubra a palavra;' \
                        '\nFase 2 - Adivinhe o número em 10 tentativas;' \
                        '\nFase 3 - Me ganhe em um pedra, papel, tesoura.\n'
                    )

                    continuar = input('Leitura feita? [S]im [N]ão \n(se não, você irá voltar para o menu inicial): ')

                    if len(continuar) >1:
                        print('escreva somente uma letra!!')
                        continue
                    continuar = continuar.lower()
                    if not continuar in 'sn' or continuar in ' ':
                        print('Escolha escrevendo ou "S" ou "N"!!')
                        continue

                    if continuar == 's':
                        os.system('clear')
                        print('Primeiro jogo... COMECE!!')
                        palavra_formada = ''
                        letras_acertadas = ''

                        while True:

                            palavra_secreta = 'desenvolvedor'

                            letra_user = input('Digite uma letra ou a palavra secreta: ')
                            letra_user = letra_user.lower()

                            if not letra_user == palavra_secreta:
                                if len(letra_user) > 1:
                                    os.system('clear')
                                    print('Se você tentou adivinhar a palavra, tente de novo. Caso contrário, insira somente uma LETRA por vez!!')
                                    continue
                                if not letra_user.isalpha():
                                    os.system('clear')
                                    print('Se você tentou adivinhar a palavra, tente de novo. Caso contrário, insira somente uma LETRA por vez!!')
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
                                    continuar = input('Pronto? [S]im [N]ão \n(se não, você voltará para o menu.): ')
                                    continuar = continuar.lower()
                                    if len(continuar) >1:
                                        print('Escreva uma letra por vez.')
                                        continue
                                    if not continuar in 'sn' or continuar in ' ':
                                        print('Escreva uma letra por vez.')
                                        continue
                                    if continuar == 's':
                                        proximo = True
                                        break
                                    if continuar == 'n':
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
                                acabar = True
                                break
                        if acabar:
                            break
                        
                        os.system('clear')
                        print('Parabéns, você acertou o número! Passaremos para a última fase.')
                        while True:
                            continuar = input('Pronto para a última fase? [S]im [N]ão \n(Se não, irá voltar para o menu): ')
                            continuar = continuar.lower()
                            if len(continuar) >1:
                                os.system('clear')
                                continue
                            if not continuar in 'sn' or continuar in ' ':
                                os.system('clear')
                                continue
                            if continuar == 's':
                                break
                            if continuar == 'n':
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
                            acabar = True
                        elif vitoria >1:
                            while True:
                                print('Parabéns, você ganhou o jogo do "bem" e ganhou uma conquista!! \
                                    \nVeja sua conquista na opção "Conquistas"')
                                
                                conquistas.append('Jogo "Bem" feito.')
                                continuar = input('Continuar? [S]im [N]ão \n(Se não, o jogo acabará / Se sim, o jogo voltará ao menu): ')
                                if len(continuar) >1:
                                    os.system('clear')
                                    continue
                                if not continuar in 'sn' or continuar in ' ':
                                    os.system('clear')
                                    continue
                                if continuar == 's':
                                    menu = True
                                    break
                                if continuar == 'n':
                                    acabar = True
                                    break

                        break
                    
                    if continuar == 'n':
                        break
                if acabar or menu:
                    break
            if continuar == 'n':
                menu = True
                break
        if acabar or menu:
            break
    if acabar:
        break
