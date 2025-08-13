import random
import os
acabar = False
sorteado = random.randint(1,20)
derrota = 0
vitoria = 0
conquistas = []

while True:
    os.system('cls')
    caminho=input('Escolha seu caminho: [B]em ou [M]al (Acaso tenha ganhado algum, selecione o outro) ')

    if len(caminho) > 1 or not caminho.isalpha():
        print('Escolha o caminho somente digitando "B" ou "M"')

    caminho=caminho.lower()

    if not caminho in 'bm':
        print('Escolha o caminho somente digitando "B" ou "M"')

    while caminho == 'b':

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
                os.system('cls')
                print(
                    'Continuaremos para o jogo, serão 3 partes:\n' \
                    '\nFase 1 - Descubra a palavra;' \
                    '\nFase 2 - Adivinhe o número em 10 tentativas;' \
                    '\nFase 3 - Me ganhe em um pedra, papel, tesoura.\n'
                )

                continuar = input('Leitura feita? [S]im [N]ão (se não, você irá voltar para a escolha de caminho) ')

                if len(continuar) >1:
                    print('escreva somente uma letra!!')
                    continue
                continuar = continuar.lower()
                if not continuar in 'sn' or continuar in ' ':
                    print('Escolha escrevendo ou "S" ou "N"!!')
                    continue

                if continuar == 's':
                    os.system('cls')
                    print('Primeiro jogo... COMECE!!')

                    while True:

                        palavra_secreta = 'desenvolvedor'

                        letra_user = input('Digite uma letra: ')
                        letra_user = letra_user.lower()
                        palavra_formada = ''

                        if letra_user == palavra_secreta:
                            os.system('cls')
                            print('Parabéns, você passou para a segunda fase, continue assim!!')
                            continuar = input('Pronto? [S]im [N]ão (se não, o jogo acabará aqui.) ')
                            continuar = continuar.lower()
                            if len(continuar) >1:
                                print('Escreva uma letra por vez, reescreva a palavra para continuar.')
                                continue
                            if not continuar in 'sn' or continuar in ' ':
                                print('Escreva uma letra por vez, reescreva a palavra para continuar.')
                                continue
                            if continuar == 's':
                                break
                            if continuar == 'n':
                                acabar = True
                                break

                        if len(letra_user) > 1:
                            print('Se você tentou adivinhar a palavra, tente de novo. caso contrário, insira somente uma letra por vez!!')
                            continue

                        for letra in palavra_secreta:
                            if letra_user == letra:
                                palavra_formada +=letra
                            else:
                                palavra_formada +='*'
                            
                        print(palavra_formada)
                    
                    #fase 2
                    if acabar:
                        break

                    os.system('cls')

                    print('Vamos continuar para a fase 2... Que comece o segundo jogo!!')
                    
                    for tentativa in range(10):

                        numero = input(f'Adivinhe o número de 1 a 20 em 10 tentativas, tentativa {tentativa}/10 \
                            Número de escolha: '                                       
                            )
                        if not numero.isdigit():
                            print('Escreva somente números!')
                            continue
                        numero = int(numero)
                        
                        if numero > sorteado:
                            print('Digite um número menor!')
                        elif numero < sorteado:
                            print('Digite um número maior!')
                        else:
                            print('Parabéns')
                            break
                    if tentativa == 9:
                        os.system('cls')
                        print('Game over!!')
                        acabar = True
                    if acabar:
                        break
                    
                    os.system('cls')
                    print('Parabéns, você acertou o número! Passaremos para a última fase.')
                    while True:
                        continuar = input('Pronto? [S]im [N]ão (se não, o jogo acabará aqui.) ')
                        continuar = continuar.lower()
                        if len(continuar) >1:
                            print('Escreva uma letra por vez, reescreva a palavra para continuar.')
                            continue
                        if not continuar in 'sn' or continuar in ' ':
                            print('Escreva uma letra por vez, reescreva a palavra para continuar.')
                            continue
                        if continuar == 's':
                            break
                        if continuar == 'n':
                            acabar = True
                            break

                    if acabar:
                        break
                    
                    #fase 3
                    os.system('cls')
                    tentativa = 0

                    while tentativa <3:
                        opcao = {
                            1: 'pedra',
                            2: 'papel',
                            3: 'tesoura'
                        }
                        escolha = random.randint(1,3)
                        jankenpon = opcao[escolha]

                        player = input(f'O jogo agora será jankenpon melhor de 3. (Escreva ou "Pedra", ou "Papel", ou "Tesoura"), prepare-se... \n(Tentativa: {tentativa}) \
                                       \n3...2...1... Jogue!! ')
                        if player.isdigit():
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue
                        if not player.isalpha():
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue
                        if len(player) <5:
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue

                        player = player.lower()

                        if player == jankenpon:
                            print("Empate!")
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
                    os.system('cls')

                    if derrota > 1:
                        print('Você perdeu tudo, seu jogo acabou!')
                        acabar = True
                    elif vitoria >1:
                        print('Parabéns, você ganhou o jogo do bem e ganhou uma conquista \
                              \nVeja sua conquista na opção "Conquistas"')
                        
                        conquistas.append('Jogo "Bem" feito.')
                        continuar = input('Continuar? [S]im [N]ão (Se não, o jogo acabará / Se sim, o jogo voltará ao menu)')
                        if len(continuar) >1:
                            print('Escreva uma letra por vez, reescreva a palavra para continuar.')
                            continue
                        if not continuar in 'sn' or continuar in ' ':
                            print('Escreva uma letra por vez, reescreva a palavra para continuar.')
                            continue
                        if continuar == 's':
                            break
                        if continuar == 'n':
                            acabar = True
                            break

                    break
                
                if continuar == 'n':
                    break

            elif continuar == 'n':
                break
        if acabar:
            break
    if acabar:
        break
