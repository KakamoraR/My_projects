import random, time, os, palavras, sys

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sair_telas():

        sair = input('\nPara sair, digite qualquer coisa: ')

        if sair != '':
            return sair

def tempo(segundos):
    global mode
    time.sleep(segundos if mode == '2' else 0)

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
        if continuar not in '12' or not continuar:
            continue
        if continuar[0] == '2':
            return False
        return
        
def modo():
    while True:
        limpar()
        mode = input('Selecione um modo: \n1)Speedrun \t2)História\n')
        if mode not in '12' or not mode:
            continue
        return mode

def perda():
    limpar()
    print('Infelizmente, você perdeu.')
    time.sleep(2)
    return True

def verificar_conquistas():
    global conquistas, tempo_inicial

    if len(conquistas) == 16 and not '100%' in conquistas:
        conquistas.append('100%')

    if time.time() - tempo_inicial <= 1800 and '100%' in conquistas and not 'Speedrunner' in conquistas:
        conquistas.append('Speedrunner')

    if len(conquistas) == 18 and not 'Platinado' in conquistas:
        conquistas.append('Platinado')

def caminho_bem():
    global pity, conquistas

    while True:
        if continuar() == False:
            break

        limpar()

        print('Vamos para a primeira fase do caminho do bem, adivinhe a palavra!!!')
        tempo(2)

        palavra_secreta = palavras.palavra_aleatoria().lower()
        letras_certas = ''
        palavra_formada = ''

        limpar()

        erro = False

        while True:
            resposta_usuario = input('Digite uma letra ou uma palavra: ')

            if not resposta_usuario.isalpha() or len(resposta_usuario) > 1:
                limpar()
                print(palavra_formada if palavra_formada else 'Digite uma letra ou a palavra secreta')
                continue

            palavra_formada = ''

            if resposta_usuario.lower() == palavra_secreta:
                break

            if resposta_usuario.lower() in palavra_secreta:
                letras_certas += resposta_usuario.lower()
            else:
                erro = True

            for letra in palavra_secreta:
                if letra in letras_certas:
                    palavra_formada += letra
                else:
                    palavra_formada += '*' 
            
            limpar()

            if palavra_formada == palavra_secreta:
                print('Parabéns, você passou para a próxima fase!')
                tempo(2)
                break

            print(palavra_formada)

        if not erro and not 'Experto' in conquistas:
            conquistas.append('Experto')
        
        if continuar() == False:
            break

        limpar()

        print('Vamos para a segunda fase do caminho do bem, adivinhe o número de 1 a 20 em 5 tentativas!!!')
        tempo(2)

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
                print('Parabéns, você passou para a próxima fase!')
                if tentativa == 0 and not 'De Primeira' in conquistas:
                    conquistas.append('De Primeira')
                tempo(2)
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
            perda()
            break
        elif continuar() == False:
            break

        limpar()

        print('Vamos para a terceira fase do caminho do bem, ganhe um jankenpon melhor de 3!!!')
        tempo(2)

        limpar()

        empates = 0
        vitorias = 0
        derrotas = 0

        while True:

            computador = random.randint(1, 3)

            player = input('Escolha entre: \n1)Pedra \t2)papel \t3)Tesoura\n')

            limpar()

            if not player.isdigit() or not player in '123':
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
            perda()
            break
        else:
            print('Parabéns, você zerou o Caminho do Bem')
            pity += 1

        if ((pity >= 15 and not 'katana' in itens_obtidos) or \
            (random.randint(1,30) == 1 and not 'Katana' in itens_obtidos)):
            conquistas.append('Katana')
            itens_obtidos.append('Katana')
        if len(itens_obtidos) == 5 and not 'Full set' in conquistas:
            conquistas.append('Full set')
        if vitorias == 2 and derrotas == 0 and empates == 0 and not 'Achei Fácil' in conquistas:
            conquistas.append('Achei Fácil')
        if not 'Caminho do Bem' in conquistas:
            conquistas.append('Caminho do Bem')

        time.sleep(2)
        break

def caminho_mal():
    global itens_obtidos, itens_uso, armas, armaduras, perdeu, ultimo_nivel

    while True:

        if continuar() == False:
            break

        limpar()

        print('Vamos para a primeira fase do caminho do Mal, digite na sequência!!!')
        tempo(2)

        nivel = 0

        while True:
            numero_rapido = ''

            limpar()
            print(f'Preparar... apontar... vai!! \tnivel:{nivel+1}/3')
            time.sleep(2)
            limpar()

            if nivel == 0:
                for i in range(0,4):
                    numero_rapido += str(random.randint(0,9))
                print(numero_rapido)
                time.sleep(0.6)
            elif nivel == 1:
                for i in range(0,6):
                    numero_rapido += str(random.randint(0,9))
                print(numero_rapido)
                time.sleep(0.8)
            elif nivel == 2:
                for i in range(0,8):
                    numero_rapido += str(random.randint(0,9))
                print(numero_rapido)
                time.sleep(1)

            while True:
                limpar()

                numero_visto = input('Número visto: ')

                if not numero_visto.isdigit():
                    continue

                break

            if numero_visto == numero_rapido:
                limpar()
                nivel += 1
                if nivel == 3:
                    print('Parabéns, você passou para a próxima fase!')
                    tempo(2)
                    break
                print('Parabéns, você passou de nível!')
                tempo(2)
            else:
                perdeu = perda()
                break

        if perdeu:
            break

        if not 'Visão' in conquistas:
            conquistas.append('Visão')

        if continuar() == False:
            break

        limpar()
        print('Vamos para a segunda fase do caminho do Mal, mini RPG!!!')
        tempo(2)

        while True:
            limpar()

            print(f'Estes são seus itens equipados atualmente: \n\narma: {itens_uso[0]} \narmadura: {itens_uso[1]}')

            continuacao = input('\nPronto? \n1)Sim \t2)Não \nEscolha: ')

            if not continuacao.isdigit() or not continuacao in '12':
                continue
            if continuacao == '2':
                perdeu = True
                break

            limpar()
            print('O player estava entendiado em sua casa, e queria se divertir de alguma forma...')
            tempo(3)
            limpar()
            print('Depois de um tempo, o player decidiu sair por ai com alguma garota que encontrasse, para talvez ter um clima entre eles.')
            tempo(3)
            limpar()
            print('Após sair pela vila, achou uma garota que era de seu tipo, e a convidou para passear pelo bosque.')
            tempo(3)
            limpar()
            print('Ambos estavam curtindo a voltinha que estavam dando, até se aproximarem um pouco mais e...Urrrrrr')
            tempo(3)
            limpar()
            print('Essa não, um zombie!!!')
            tempo(3)
            limpar()
            print('Após esse momento, player se prepara para o combate')
            tempo(3)

            enuma = False
            vida_player = 100
            vida_monstro = 30
            vida_boss = 70
            sangramento = False

            while True:
                if vida_player <= 0:
                    perdeu = perda()
                    break
                elif vida_boss <= 0:
                    break

                limpar()
                
                if itens_uso[0] == 'excalibur':
                    dano_a_mais = 7 
                    enuma = True
                elif itens_uso[0] == 'espada':
                    dano_a_mais = 4
                elif itens_uso[0] == 'katana':
                    dano_a_mais = 10
                else:
                    dano_a_mais = 0

                if itens_uso[1] == 'capacete':
                    defesa = 4
                elif itens_uso[1] == 'peitoral':
                    defesa = 7
                else:
                    defesa = 0

                dado = random.randint(1,20)

                if dado == 20 and enuma and not 'Gilga reference' in conquistas:
                    conquistas.append('Gilga reference')
                    if not 'Vinte natural' in conquistas:
                        conquistas.append('Vinte natural')
                elif dado == 20 and not 'Vinte natural' in conquistas:
                    conquistas.append('Vinte natural')

                dano_player = 99999 if enuma == True and dado == 20 else (dado + dano_a_mais + (5 if itens_uso[0] and dado == 20 else 0))

                print(f'Player jogou o dado e conseguiu {dado}')
                tempo(2)
                if enuma:
                    print('Player sente um poder surgir em suas veias.')
                    time.sleep(2)
                    print('Player - Enuma... Eilish!!!')
                else:
                    print(f'Player deu {dano_player} de dano.')
                time.sleep(2)

                limpar()

                if sangramento:
                    print('Player está sangrando... -5 de vida')
                    vida_player -= 5
                    sangramento = False
                    print(f'Player está com {vida_player if vida_player > 0 else 0} de vida')
                    time.sleep(2)
                    limpar()

                ataques_monstros = [
                    ["golpe simples", 12],
                    ["mordida", 10],
                    ["espancada", 33]
                ]

                ataque_monstro = random.randint(0,1) if vida_monstro > 0 else random.randint(0,2)

                if ataque_monstro == 1:
                    sangramento = True

                if vida_monstro > 0:

                    vida_monstro -= dano_player

                    if vida_monstro <= 0:
                        print('Párabens, você derrotou o monstro!')
                        time.sleep(2)
                        limpar()
                        print('Espera... tem outro gigante bem ali!')
                        time.sleep(2)
                        continue
                    else:
                        print(f'Monstro está com {vida_monstro} de vida')
                        time.sleep(2)

                    limpar()
                    print('Vez do monstro atacar.')
                    tempo(2)
                    print(f'Monstro usou {ataques_monstros[ataque_monstro][0]} e deu {ataques_monstros[ataque_monstro][1]}')
                    if sangramento:
                        print('Player está sangrando... -5 de vida')
                        vida_player -= 5
                    time.sleep(2)

                    vida_player -= ataques_monstros[ataque_monstro][1] + defesa

                    limpar()
                    print(f'Player está com {vida_player if vida_player > 0 else 0} de vida')
                    time.sleep(2)

                else:

                    vida_boss -= dano_player

                    if vida_boss <= 0:
                        continue
                    else:
                        print(f'Boss está com {vida_boss} de vida')
                        time.sleep(2)

                    limpar()
                    print('Vez do boss atacar.')
                    tempo(2)
                    print(f'Boss usou {ataques_monstros[ataque_monstro][0]} e deu {ataques_monstros[ataque_monstro][1]} de dano')
                    if sangramento:
                        print('Player está sangrando... -5 de vida')
                        vida_player -= 5
                    time.sleep(2)

                    vida_player -= ataques_monstros[ataque_monstro][1] + defesa

                    limpar()
                    print(f'Player está com {vida_player if vida_player > 0 else 0} de vida')
                    time.sleep(2)

            break

        if perdeu:
            break

        if random.randint(1,12) == 1 and not 'Espada' in conquistas:
            conquistas.append('Espada')
            itens_obtidos.append('Espada')
        if random.randint(1,12) == 1 and not 'Capacete' in conquistas:
            conquistas.append('Capacete')
            itens_obtidos.append('Capacete')
        if random.randint(1,12) == 1 and not 'Peitoral' in conquistas:
            conquistas.append('Peitoral')
            itens_obtidos.append('Peitoral')
        if random.randint(1,12) == 1 and not 'Excalibur' in conquistas:
            conquistas.append('Excalibur')
            itens_obtidos.append('Excalibur')
        if len(itens_obtidos) == 5 and not 'Full set' in conquistas:
            conquistas.append('Full set')
        if vida_player >= 50 and not 'Peito de Ferro' in conquistas:
            conquistas.append('Peito de Ferro')

        limpar()
        print('Parabéns, você derrotou os monstros e passou para a próxima fase!')
        time.sleep(2)

        if continuar() == False:
            break

        limpar()
        print('Vamos para a terceira fase do caminho do Mal, boa sorte!!!')
        tempo(2)

        while True:

            limpar()
            cara_coroa_usuario = input('Escolha entre... \n1)cara \t2)coroa. \nEscolha: ')

            if not cara_coroa_usuario.isdigit() or not cara_coroa_usuario in '12':
                continue

            if cara_coroa_usuario == random.randint(1,2):
                print('parabéns, você zerou o caminho do Mal!')
                if not 'Caminho do Mal' in conquistas:
                    conquistas.append('Caminho do Mal')
                if not 'Ez game' in conquistas:
                    conquistas.append('Ez game')
            else:
                perdeu = perda()
                ultimo_nivel = True
                break
        
        if perdeu:
            break

def conquista():

    global conquistas
    
    while True:

        limpar()

        print('Segue conquistas ganhas até agora: \n')

        for a, b in enumerate(conquistas):
            print(a+1, b, sep='-')

        if sair_telas():
            break

def regras():
    global mode, pity, conquistas

    while True:
    
        limpar()

        print(
            'Regras do jogo:'\
            '\n1-Equipe os itens para poder usá-los na segunda fase do caminho do mal'\
            '\n2-Você pode deixar o jogo mais rapido de zerar mudando o modo nas regras'\
            '\n3-Você pode manter equipado uma arma e uma armadura por vez'\
            '\n4-O sangramento dura 2 turnos'\
            '\n5-O modo não altera informações consideradas importantes na segunda fase do mal'\
            '\n6-Por padrão, o modo do jogo vem como modo história'\
            '\n6-Se vira'\
            '\n\nConquistas do jogo:'\
            '\n1-"Experto", consegue ao passar a primeira fase do bem sem errar uma letra'\
            '\n2-"De Primeira", consegue ao acertar de primeira o numero da segunda fase do bem'\
            '\n3-"Katana", consegue ao pegar a "Katana" depois de zerar o caminho do bem'\
            '\n4-"Achei Fácil", consegue ao passar a terceira fase do bem sem empatar ou perder'\
            '\n5-"Caminho do Bem", consegue ao zerar o caminho do bem'\
            '\n6-"Visão", consegue ao passar a primeira fase do mal'\
            '\n7-"Vinte natural", consegue ao tirar um 20 no dado da segunda fase do mal'\
            '\n8-"Gilga reference", consegue ao tirar um 20 no dado da segunda fase do mal com a "Excalibur"'\
            '\n9-"Espada", consegue ao pegar a "Espada" da segunda fase do mal'\
            '\n10-"Excalibur", consegue ao pegar a "Excalibur" da segunda fase do mal'\
            '\n11-"Capacete", consegue ao pegar a "Capacete" da segunda fase do mal'\
            '\n12-"Peitoral", consegue ao pegar a "Peitoral" da segunda fase do mal'\
            '\n13-"Full set", consegue ao pegar todos os itens do jogo'\
            '\n14-"Peito de Ferro", consegue ao passar a segunda fase do mal sem perder mais de 50 de vida'\
            '\n15-"Ez game", consegue ao passar a terceira fase do mal na primeira tentativa'\
            '\n16-"Caminho do Mal", consegue ao zerar o caminho do mal'\
            '\n17-"100%", consegue ao pegar todas as 16 conquistas anteriores'\
            '\n18-"Speedrunner", consegue ao zerar o jogo em 30 minutos'\
            '\n19-"Platinado", consegue ao pegar todas as conquistas do jogo'\
            )

        tempo_atual = time.time() - tempo_inicial
        print(
            f'\nTempo de jogo: {tempo_atual:.2f} segundos\n' \
            'Pity para item:', f'{pity}/15' if pity <= 15 else '15/15', '(Item obtido)' if 'Katana' in conquistas else '(Item não obtido)'
            )
        print('\nPara mudar o modo, digite "1"')

        saida = sair_telas()
    
        if saida == '1':
            mode = modo()
        elif saida is None:
            continue
        else:
            break

def sair():
    limpar()
    sys.exit()

def itens():
    global itens_obtidos, itens_uso, armas, armaduras

    while True:
    
        limpar()

        print('Itens obtidos até o momento:\n')
        for a, b in enumerate(itens_obtidos):
            print(a+1, b, sep='-')

        print('\nItens em uso no momento:\n')
        for c,d in enumerate(itens_uso):
            if d:
                print(d)

        equipar = input('\nSe deseja equipar algum item, digite o nome aqui.\n(Para sair digite qualquer coisa)\nEscolha: ')

        if equipar.isalpha():
            equipar = equipar.lower()

        if equipar.capitalize() in itens_obtidos:
            if equipar in armas:
                itens_uso[0] = equipar
            elif equipar in armaduras:
                itens_uso[1] = equipar
        elif equipar:
            break

conquistas = []
itens_obtidos = []
armas = ['katana', 'espada', 'excalibur']
armaduras = ['peitoral', 'capacete']
itens_uso = ['', '']
pity = 0
mode = '2'
ultimo_nivel = False
tempo_inicial = time.time()

while True:
    perdeu = False

    verificar_conquistas()

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
        conquista()
    elif caminho == '6':
        sair()
