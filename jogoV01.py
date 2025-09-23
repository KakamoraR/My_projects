#tempo usado para a criação do código: 25h
import time
import palavras
import random
import os
acabar = False
conquistas = [] 
itens = [] #itens em geral
uso = ['',''] #Itens sendo usados
arma = ['excalibur', 'sabre', 'espada']
armadura = ['capacete', 'peitoral', 'refletor']
passou = False
record = time.time()
derrotado = False
pity = 0

while True:
    sorteado = random.randint(1,20)
    four_digit = random.randint(1000,9999)
    six_digit = random.randint(100000,999999)
    eight_digit = random.randint(10000000,99999999)
    derrota = 0
    vitoria = 0
    empate = 0
    dano_a_mais = 0
    defesa = 0
    ataque_basico = 10
    ataque_secundario = 12
    ataque_especial = 33
    menu = False
    next = False
    sangramento = False
    erro = False

    if derrotado:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        derrotado = False
        print('Você perdeu')
        time.sleep(3)

    item = random.randint(1,500)
    if item == 500:
        if not 'refletor' in itens:
            itens.append('refletor')

    if len(conquistas) == 15:
        if not '100%' in conquistas:
            conquistas.append('100%')

    if '100%' in conquistas:
        parada = time.time()
        if parada - record <= 1800:
            if not 'Speedrunner' in conquistas:
                conquistas.append('Speedrunner')
    
    if 'Speedrunner' in conquistas:
        if not 'Platinado' in conquistas:
            conquistas.append('platinado')

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
                    '\nFase 2 - Adivinhe o número em 5 tentativas;' \
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
                        else:
                            erro = True
                        
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
                                if erro==False:
                                    if not 'no pain no gain' in conquistas:
                                        conquistas.append('no pain no gain')
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
                            if tentativa == 0:
                                if not 'primeira tentativa' in conquistas:
                                    conquistas.append('primeira tentativa')
                            break
                        if tentativa == 5:
                            derrotado = True
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

                        verificacao = False

                        opcao = ['pedra','papel','tesoura']
                        escolha = random.randint(0,2)
                        jankenpon = opcao[escolha]

                        player = input(f'prepare-se...3...2...1... Jogue!!: ')
                        if not player.isalpha():
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue
                        player = player.lower()
                        for jogada in opcao:
                            if player == jogada:
                                verificacao = True
                        if not verificacao:
                            if os.name == "nt":
                                os.system('cls')
                            else:
                                os.system('clear')
                            print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                            continue

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
                            print('Você Perdeu')
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
                        derrotado = True
                        menu = True
                    elif vitoria >1:
                        while True:
                            print('Parabéns, você ganhou o jogo do bem e ganhou uma conquista!! \n(A não ser que já tenha ganhado antes)')
                            
                            if vitoria == 2 and empate == 0 and derrota == 0:
                                if not 'achei fácil' in conquistas:
                                    conquistas.append('achei fácil')

                            item = random.randint(1, 30)
                            
                            pity += 1
                            if item == 1 and not 'sabre' in conquistas or pity == 15 and not 'sabre' in conquistas:
                                itens.append('sabre')
                                conquistas.append('sabre')
                                if 'sabre' in conquistas and 'espada' in conquistas and 'excalibur' in conquistas and 'capacete' in conquistas and 'peitoral' in conquistas and not 'Set completo' in conquistas:
                                    conquistas.append('Set completo')
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
                                acabar = True
                                break
                        if acabar:
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
                                        continue
                                    num_user = int(num_user)
                                    if num_user == four_digit or num_user == six_digit:
                                        nivel +=1
                                        while True:
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')
                                            print('Parabéns, você passou para o próximo nível')
                                            continuar = input('Pronto? [S]im [N]ão (Se não você voltará ao menu) ')

                                            if not continuar.isalpha():
                                                continue
                                            continuar = continuar.lower()
                                            if not continuar[0] in 'sn':
                                                continue
                                            break
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
                                        derrotado = True
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
                            enuma = False
                            refletor = False
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

                                        if uso[0] in armadura:
                                            if uso[0] == 'capacete':
                                                defesa = 4
                                            elif uso[0] == 'peitoral':
                                                defesa = 7
                                            elif uso[0] == 'refletor':
                                                refletor = True
                                            else:
                                                defesa = 0
                                        if uso[1] in arma:
                                            if uso[0] == 'excalibur':
                                                dano_a_mais = 7
                                            elif uso[0] == 'espada':
                                                dano_a_mais = 4
                                            elif uso[0] == 'sabre':
                                                dano_a_mais = 10
                                            else:
                                                dano_a_mais = 0
                                        
                                        if vida_player <=0:
                                            derrotado = True
                                            menu = True
                                            break

                                        if vida_boss <= 0:
                                            print('O player derrotou os monstros!!')
                                            if vida_player >=50:
                                                if not 'nem senti' in conquistas:
                                                    conquistas.append('nem senti')
                                            time.sleep(3)
                                            item = random.randint(1,8)
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
                                            if 'sabre' in conquistas and 'espada' in conquistas and 'excalibur' in conquistas and 'capacete' in conquistas and 'peitoral' in conquistas and not 'Set completo' in conquistas:
                                                conquistas.append('Set completo')
                                            break

                                        dano = 0
                                        dado = random.randint(1,20)
                                        ataque = random.randint(1,3)

                                        if dado == 20:
                                            if not 'vinte natural' in conquistas:
                                                conquistas.append('vinte natural')
                        
                                        if uso[0] in arma and dado == 20:
                                            if 'excalibur' in uso[0]:
                                                enuma = True
                                            else:
                                                dano = 25 + dano_a_mais
                                        else:
                                            dano = dado + dano_a_mais
                                        
                                        print(f'Ataque de player, jogando o dado...')
                                        time.sleep(1.5)
                                        print(dado)
                                        time.sleep(1.5)
                                        if enuma:
                                            if not 'Gilga reference' in conquistas:
                                                conquistas.append('Gilga reference')
                                            print('player sente um poder surgir...')
                                            time.sleep(2)
                                            print('Player - "Enuma... Eilish!"')
                                            time.sleep(2)
                                            print('Um grande raio atinge o monstro dando hitkill')
                                            time.sleep(2)
                                        else:
                                            print(f'player deu {dano} de dano!')
                                            time.sleep(3)
                                        if sangramento:
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')
                                            print('Player está sangrando (-5)')
                                            vida_player -= 5
                                            print(f'Player está com {vida_player} de vida')
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
                                            if enuma:
                                                vida_boss = 0
                                            print(f'O Boss está com {vida_boss} de vida')
                                            if enuma:
                                                enuma = False
                                                continue
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
                                            if refletor:
                                                vida_boss = vida_boss - ataque[1]
                                                print(f'O ataque foi refletido, o boss tomou seu próprio ataque.' \
                                                f'\nO boss está com {vida_boss} de vida')
                                                time.sleep(3)
                                            else:
                                                vida_player = vida_player - ataque[1] + defesa
                                            if ataque[0] == 'mordida' and not refletor:
                                                sangramento = True
                                                vida_player -= 5
                                                print('Player está sangrando (-5)')
                                                time.sleep(3)
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')
                                            if not refletor:
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
                                                if enuma:
                                                    vida_monstro = 0
                                                print(f'O monstro está com {vida_monstro} de vida')
                                                time.sleep(3)
                                                if enuma:
                                                    enuma = False
                                                    continue
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
                                                if refletor:
                                                    vida_monstro = vida_monstro - ataque[1]
                                                    print(f'O ataque foi refletido, o monstro tomou seu próprio ataque.' \
                                                    f'\nO monstro está com {vida_monstro} de vida')
                                                    time.sleep(3)
                                                else:
                                                    vida_player = vida_player - ataque[1] + defesa
                                                if ataque[0] == 'mordida' and not refletor:
                                                    sangramento = True
                                                    vida_player -= 5
                                                    print('Player está sangrando (-5)')
                                                    time.sleep(3)
                                                if os.name == 'nt':
                                                    os.system('cls')
                                                else:
                                                    os.system('clear')
                                                if not refletor:
                                                    print(f'Player está com {vida_player} de vida')
                                                    time.sleep(3)                                    
                                        
                                    if continuar[0] == 'n' or menu:
                                        menu = True
                                        break

                                    break

                                if menu:
                                    break
                                    
                                while True:

                                    if os.name == 'nt':
                                        os.system('cls')
                                    else:
                                        os.system('clear')

                                    print('Você passou para a terceira fase do caminho do mal, parabéns!!')                   
                                    
                                    continuar = input('Pronto para o que há de vir? [S]im [N]ão ')
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

                                        moeda = random.randint(1,2)
                                        if moeda == 1:
                                            moeda = 'cara'
                                        else: 
                                            moeda = 'coroa'

                                        escolha = input('Faça a escolha certa:'
                                        '\nCara ou Coroa?\n')
                                        if not escolha.isalpha():
                                            continue
                                        escolha = escolha.lower()
                                        if not escolha in 'caracoroa':
                                            continue
                                        if os.name == 'nt':
                                            os.system('cls')
                                        else:
                                            os.system('clear')

                                        while escolha == moeda:
                                            if os.name == 'nt':
                                                os.system('cls')
                                            else:
                                                os.system('clear')
                                            print('Parabéns, você ganhou o caminho do mal! \nJunto disso ganhou também uma conquista e perda de tempo de vida')
                                            if not 'Caminho do mal' in conquistas:
                                                conquistas.append('Caminho do mal')
                                            if not passou:
                                                if not 'first try' in conquistas:
                                                    conquistas.append('first try')
                                            passou = True
                                            voltar = input('Deseja voltar ao menu?' \
                                            '\n(Se "não" você sairá do jogo) ')
                                            if not voltar.isalpha():
                                                continue
                                            voltar = voltar.lower()
                                            if not voltar[0] in 'sn':
                                                continue
                                            if voltar[0] =='s':
                                                menu = True
                                                break
                                            if voltar[0] =='n':
                                                acabar = True
                                                break

                                        if moeda != escolha:
                                            derrotado = True
                                            menu = True
                                            break
                                        if menu or acabar:
                                            break

                                    if continuar[0] == 'n' or menu or acabar:
                                        menu = True
                                        break
                                if continuar[0] == 'n' or menu or acabar:
                                    menu = True
                                    break
                            if continuar[0] == 'n' or menu or acabar:
                                menu = True
                                break
                if continuar[0] == 'n' or menu or acabar:
                    menu = True
                    break
            if menu or acabar:
                break
        if continuar[0] == 'n' or menu or acabar:
            break
    while caminho[0] == 'r':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print('Para deixar mais claro, esse jogo possui algumas regras e explicações:\n' \
        '\n1 - Acaso perder algum desafio, o jogo te trará para o menu.' \
        '\n2 - O nível do bem é mais fácil do que o nível do mal, \napesar disso, você dependerá MUITO da sua sorte para passar.' \
        '\n3 - Você pode ganhar itens que te ajudarão a derrotar os monstros\nNo caminho do mal.' \
        '\n4 - É possível "Platinar" o jogo, enquanto isso, o tempo corre.' \
        '\n5 - O final do caminho do mal é desagradável.' \
        '\n6 - Há 17 conquistas no tal.' \
        '\n7 - Há uma conquista por fase, menos a primeria fase do mal.' \
        '\n\nVeja como adquirir as conquistas:' \
        '\n\nPlatinado - Adquira todas as conquistas (*CONQUISTA PERDÍVEL*)' \
        '\n\n100% - Complete o jogo 100% (todas as conquistas, exceto Platinado e Speedrunner) (*CONQUISTA PERDÍVEL*)' \
        '\nSpeedrunner - Adquira a conquista 100% entro de 30 minutos desde o novo jogo (*CONQUISTA PERDÍVEL*)' \
        '\n\nNo Pain, No Gain - Durante a Fase 1 do Caminho do Bem, não erre nenhuma letra' \
        '\nPrimeira Tentativa - Durante a Fase 2 do Caminho do Bem, acerte o número na primeira tentativa' \
        '\nAchei Fácil - Durante a Fase 3 do Caminho do Bem, adquira apenas 2 vitórias, sem empates e derrotas' \
        '\nJogo "Bem" Feito - Conclua o Caminho do Bem' \
        '\n\nNem Senti - Durante a Fase 2 do Caminho do Mal, mate o chefe sobrando mais de 50 pontos de vida' \
        '\nVinte Natural - Durante a Fase 2 do Caminho do Mal, role um 20 no dano' \
        '\nGilga reference - Acerte um crítico usando a excalibur' \
        '\nCaminho do Mal - Conclua o Caminho do Mal' \
        '\nFirst Try - Complete o Caminho do Mal na primeira tentativa (desde um novo jogo) (*CONQUISTA PERDÍVEL*)' \
        '\n\nSabre - Adquira o Sabre após concluir o Caminho do Bem' \
        '\nEspada - Adquira a Espada após concluir a luta contra os monstros' \
        '\nExcalibur - Adquira a Excalibur após concluir a luta contra os monstros' \
        '\nCapacete - Adquira a Capacete após concluir a luta contra os monstros' \
        '\nPeitoral - Adquira a Peitoral após concluir a luta contra os monstros' \
        '\nSet Completo - Adquira todos os equipamentos (Sabre, Espada, Excalibur, Capacete e Peitoral)')
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
        for quant, conq in enumerate(conquistas):
            print(f'{quant+1} "{conq}"')
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
            acabar = True
            break
        if continuar[0] == 'n':
            break
    while caminho[0] == 'i':
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
        print(f'Bem vindo a aba de itens, atualmente você possui {len(itens)}.\n')
        for numeros, material in enumerate(itens):
            print(f'{numeros+1} "{material}"')
        equipar = input('\nDeseja equipar algum item?' \
        '\n(Digite "não" para voltar ao menu, ou "limpar" para desequipar os itens) ')
        if not equipar.isalpha():
            continue
        equipar = equipar.lower()
        if equipar[0] == 'n':
            break
        elif equipar[0] == 'l':
            uso.clear()
            uso.insert(0, '')
            uso.insert(1, '')
        elif equipar in uso:
            print('Item já está em uso')
            time.sleep(2)
            continue
        elif not equipar in itens:
            print('Você não tem este item para poder usa-lo ou item não existe')
            time.sleep(2)
            continue
        elif equipar in armadura:
            if uso[0]:
                uso.remove(uso[0])
            uso.insert(0, equipar)
        elif equipar in arma:
            if uso[1]:
                uso.remove(uso[1])
            uso.insert(1, equipar)
        else:
            continue
        print(f'Item em uso: {uso[0:2]}')
        time.sleep(3)
    if acabar:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.systen('clear')
        break
