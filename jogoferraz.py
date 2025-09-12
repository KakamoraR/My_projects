import os
import random
import time
import palavras


class JogoRPGSimples:
    def __init__(self):
        self.acabar = False
        self.conquistas = []
        self.itens = []
        self.uso = [""]
        self.arma = ["excalibur", "sabre", "espada"]
        self.armadura = ["capacete", "peitoral"]
        self.passou = False
        self.record = time.time()
        self.derrotado = False

    def clear(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def leia_opcao(self, prompt: str) -> str:
        """Lê uma entrada do usuário, valida que contém letras, retorna lowercase."""
        entrada = input(prompt)
        if not isinstance(entrada, str):
            return ""
        entrada = entrada.strip().lower()
        return entrada

    def checa_conquistas_temporais(self):
        if len(self.conquistas) == 14 and "100%" not in self.conquistas:
            self.conquistas.append("100%")

        if "100%" in self.conquistas:
            parada = time.time()
            if parada - self.record <= 1800:
                if "Speedrunner" not in self.conquistas:
                    self.conquistas.append("Speedrunner")

        if "Speedrunner" in self.conquistas:
            if "platinado" not in self.conquistas:
                self.conquistas.append("platinado")

    def menu_principal(self):
        while not self.acabar:
            self.checa_conquistas_temporais()
            if self.derrotado:
                self.clear()
                self.derrotado = False
                print("Você perdeu")
                time.sleep(3)

            self.clear()
            caminho = self.leia_opcao(
                "Escolha seu caminho: \n[B]em    [R]egras        [I]tens\n"
                "[M]al    [C]onquistas    [S]air\n"
                "(Acaso tenha ganhado algum, selecione o outro): "
            )
            if not caminho or caminho[0] not in "bmrcis":
                continue

            opc = caminho[0]
            if opc == "b":
                self.caminho_bem()
            elif opc == "m":
                self.caminho_mal()
            elif opc == "r":
                self.mostrar_regras()
            elif opc == "c":
                self.mostrar_conquistas()
            elif opc == "i":
                self.menu_itens()
            elif opc == "s":
                self.sair()

    def caminho_bem(self):
        self.clear()
        continuar = self.leia_opcao("Você escolheu o caminho do bem, deseja continuar? [S]im [N]ão ")
        if not continuar or continuar[0] not in "sn":
            print("Faça uma escolha.")
            time.sleep(1)
            return
        if continuar[0] == "n":
            return

        sorteado = random.randint(1, 20)
        four_digit = random.randint(1000, 9999)
        six_digit = random.randint(100000, 999999)
        eight_digit = random.randint(10000000, 99999999)

        while True:
            self.clear()
            print(
                "Continuaremos para o jogo, serão 3 partes:\n"
                "\nFase 1 - Descubra a palavra;"
                "\nFase 2 - Adivinhe o número em 5 tentativas;"
                "\nFase 3 - Me ganhe em um pedra, papel, tesoura.\n"
            )
            continuar = self.leia_opcao("Leitura feita? [S]im [N]ão \n(se não, você irá voltar para o menu inicial): ")
            if not continuar or continuar[0] not in "sn":
                continue
            if continuar[0] == "n":
                return

            self.clear()
            print("Primeiro jogo... COMECE!!")
            palavra_formada = ""
            letras_acertadas = ""
            palavra_secreta = palavras.palavra_aleatoria().lower()
            erro = False
            menu = False
            proximo = False

            while True:
                letra_user = input("Digite uma letra ou a palavra secreta: ").strip().lower()
                if not letra_user:
                    continue

                if letra_user != palavra_secreta:
                    if len(letra_user) > 1 or not letra_user.isalpha():
                        self.clear()
                        print(
                            "Se você tentou adivinhar a palavra, tente de novo. Caso contrário, insira somente uma LETRA por vez!!"
                        )
                        print(palavra_formada)
                        continue

                palavra_formada = ""
                if letra_user in palavra_secreta:
                    letras_acertadas += letra_user
                else:
                    erro = True

                for letra in palavra_secreta:
                    if letra in letras_acertadas:
                        palavra_formada += letra
                    else:
                        palavra_formada += "*"

                self.clear()
                print(palavra_formada)

                if letra_user == palavra_secreta or palavra_formada == palavra_secreta:
                    while True:
                        self.clear()
                        if not erro and "no pain no gain" not in self.conquistas:
                            self.conquistas.append("no pain no gain")
                        print(
                            "Parabéns, você passou para a segunda fase, continue assim!!"
                            f'\nA palavra secreta era: "{palavra_secreta}"'
                        )
                        continuar = self.leia_opcao("Pronto? [S]im [N]ão \n(se não, você voltará ao menu): ")
                        if not continuar or continuar[0] not in "sn":
                            continue
                        if continuar[0] == "s":
                            proximo = True
                            break
                        else:
                            menu = True
                            break
                    break
                if menu:
                    break

            if menu:
                return

            self.clear()
            print("Vamos continuar para a fase 2... Que comece o segundo jogo!!")
            tentativa = 0
            derrotado = False
            while tentativa < 5:
                numero = input(
                    f"Adivinhe o número de 1 a 20 em 5 tentativas, tentativa {tentativa+1}/5 \nNúmero de escolha: "
                ).strip()
                if not numero.isdigit():
                    self.clear()
                    print("Escreva somente números!")
                    continue
                numero = int(numero)
                if numero > sorteado:
                    self.clear()
                    print("Digite um número menor!")
                    tentativa += 1
                elif numero < sorteado:
                    self.clear()
                    print("Digite um número maior!")
                    tentativa += 1
                else:
                    print("Parabéns")
                    if tentativa == 0 and "primeira tentativa" not in self.conquistas:
                        self.conquistas.append("primeira tentativa")
                    break

                if tentativa == 5:
                    self.derrotado = True
                    derrotado = True
                    break

            if derrotado:
                return

            self.clear()
            print("Parabéns, você acertou o número! Passaremos para a última fase.")
            while True:
                continuar = self.leia_opcao(
                    "Pronto para a última fase? [S]im [N]ão \n(Se não, irá voltar para o menu): "
                )
                if not continuar or continuar[0] not in "sn":
                    continue
                if continuar[0] == "n":
                    return
                break

            self.clear()
            tentativa = 0
            vitoria = 0
            derrota = 0
            empate = 0

            print('O jogo agora será jankenpon melhor de 3. \n(Escreva ou "Pedra", ou "Papel", ou "Tesoura")')
            while tentativa < 3:
                opcao = {1: "pedra", 2: "papel", 3: "tesoura"}
                escolha = random.randint(1, 3)
                jankenpon = opcao[escolha]

                player = input("prepare-se...3...2...1... Jogue!!: ").strip()
                if not player.isalpha() or len(player) < 5:
                    self.clear()
                    print('Escreva "Pedra", ou "Papel", ou "Tesoura"!')
                    continue
                player = player.lower()

                self.clear()
                print(f"A máquina jogou: {jankenpon} \nVocê jogou: {player}")

                if player == jankenpon:
                    print("Empate!")
                    empate += 1
                elif (
                    (player == "pedra" and jankenpon == "tesoura")
                    or (player == "papel" and jankenpon == "pedra")
                    or (player == "tesoura" and jankenpon == "papel")
                ):
                    print("Você venceu!")
                    tentativa += 1
                    vitoria += 1
                else:
                    print("Você Perdeu")
                    tentativa += 1
                    derrota += 1

                if vitoria == 2 or derrota == 2:
                    break
                print(f"\nVitórias: {vitoria} \nDerrotas: {derrota} \nEmpates: {empate}\n")

            self.clear()
            if derrota > 1:
                self.derrotado = True
                return
            elif vitoria > 1:
                print(
                    "Parabéns, você ganhou o jogo do bem e ganhou uma conquista e um item!! \n(A não ser que já tenha ganhado antes)"
                )
                if vitoria == 2 and empate == 0 and derrota == 0 and "achei fácil" not in self.conquistas:
                    self.conquistas.append("achei fácil")

                item_aleatorio = random.randint(1, 100)
                if item_aleatorio == 1 and "sabre" not in self.conquistas:
                    self.itens.append("sabre")
                    self.conquistas.append("sabre")
                    if (
                        all(x in self.conquistas for x in ("sabre", "espada", "excalibur", "capacete", "peitoral"))
                        and "Set completo" not in self.conquistas
                    ):
                        self.conquistas.append("Set completo")
                if 'Jogo "Bem" feito' not in self.conquistas:
                    self.conquistas.append('Jogo "Bem" feito')

                while True:
                    continuar = self.leia_opcao(
                        "Continuar? [S]im [N]ão \n(Se não, o jogo acabará / Se sim, o jogo voltará ao menu): "
                    )
                    if not continuar or continuar[0] not in "sn":
                        continue
                    if continuar[0] == "s":
                        return
                    else:
                        confirmar = self.leia_opcao("Deseja sair mesmo: [S]im [N]ão ")
                        if not confirmar or confirmar[0] not in "sn":
                            continue
                        if confirmar[0] == "s":
                            self.acabar = True
                            return
                        else:
                            return
            return

    def caminho_mal(self):
        self.clear()
        continuar = self.leia_opcao("Você escolheu o caminho do mal, deseja continuar? [S]im [N]ão ")
        if not continuar or continuar[0] not in "sn":
            print("Faça uma escolha.")
            time.sleep(1)
            return
        if continuar[0] == "n":
            return

        four_digit = random.randint(1000, 9999)
        six_digit = random.randint(100000, 999999)
        eight_digit = random.randint(10000000, 99999999)
        menu = False
        next_stage = False

        while True:
            self.clear()
            print(
                "Continuaremos para o jogo, serão 3 partes:\n"
                "\nFase 1 - Digite na Sequência;"
                "\nFase 2 - Mini RPG;"
                "\nFase 3 - ...\n"
            )
            continuar = self.leia_opcao("Leitura feita? [S]im [N]ão \n(se não, você irá voltar para o menu inicial): ")
            if not continuar or continuar[0] not in "sn":
                continue
            if continuar[0] == "n":
                return

            while True:
                self.clear()
                print("Vamos para o primeiro jogo... Preste bastante atenção.")
                continuar = self.leia_opcao("Pronto? [S]im [N]ão ")
                if not continuar or continuar[0] not in "sn":
                    print("Faça uma escolha")
                    continue
                if continuar[0] == "n":
                    menu = True
                    break

                nivel = 0
                while True:
                    self.clear()
                    if nivel == 0:
                        print(four_digit)
                    elif nivel == 1:
                        print(six_digit)
                    else:
                        print(eight_digit)

                    if nivel == 0:
                        time.sleep(0.6)
                    elif nivel == 1:
                        time.sleep(0.8)
                    else:
                        time.sleep(1)

                    num_user = input("Digite o número correto: ").strip()
                    if not num_user.isdigit():
                        continue
                    num_user = int(num_user)

                    if num_user == four_digit or num_user == six_digit:
                        nivel += 1
                        while True:
                            self.clear()
                            print("Parabéns, você passou para o próximo nível")
                            continuar = self.leia_opcao("Pronto? [S]im [N]ão (Se não você voltará ao menu) ")
                            if not continuar or continuar[0] not in "sn":
                                continue
                            break
                        if continuar[0] == "n":
                            menu = True
                            break
                        if nivel >= 2:
                            pass
                    elif num_user == eight_digit:
                        while True:
                            self.clear()
                            continuar = self.leia_opcao(
                                "Parabéns, você passou para a próxima fase.\npronto para continuar? [S]im [N]ão (Se não, você voltará ao menu) "
                            )
                            if not continuar or continuar[0] not in "sn":
                                continue
                            if continuar[0] == "s":
                                next_stage = True
                                break
                            else:
                                menu = True
                                break
                        if menu or next_stage:
                            break
                    else:
                        self.derrotado = True
                        menu = True
                        break

                    if menu or next_stage:
                        break

                if menu or next_stage:
                    break

            if menu:
                return
            if not next_stage:
                return

            next_stage = False
            vida_player = 100
            vida_monstro = 30
            vida_boss = 70
            defesa = 0
            dano_a_mais = 0
            ataque_basico = 10
            ataque_secundario = 12
            ataque_especial = 33
            sangramento = False

            while True:
                self.clear()
                print("Bem vindo a fase 2 do caminho do mal. Segue os dados do player:")
                print(f"\nitens: {self.uso}\nvida: {vida_player}")
                continuar = self.leia_opcao("\nPronto para começar? [S]im [N]ão (Se não, você voltará ao menu) ")
                if not continuar or continuar[0] not in "sn":
                    continue
                if continuar[0] == "n":
                    menu = True
                    break

                self.clear()
                print("O player estava entendiado em sua casa, e queria se divertir de alguma forma...")
                time.sleep(4)
                self.clear()
                print(
                    "Depois de um tempo, o player decidiu sair por ai com alguma garota que encontrasse, para talvez ter um clima entre eles."
                )
                time.sleep(4)
                self.clear()
                print(
                    "Após sair pela vila, achou uma garota que era de seu tipo, e a convidou para passear pelo bosque."
                )
                time.sleep(4)
                self.clear()
                print(
                    "Ambos estavam curtindo a voltinha que estavam dando, até se aproximarem um pouco mais e...Urrrrrr"
                )
                time.sleep(4)
                self.clear()
                print("Essa não, um zombie!!!")
                time.sleep(3)
                self.clear()
                print("Após esse momento, player se prepara para o combate")
                time.sleep(3)

                combate_em_andamento = True
                while combate_em_andamento:
                    self.clear()
                    confirmar = self.leia_opcao("Pronto para o combate? [S]im [N]ão (Se não, você voltará ao menu) ")
                    if not confirmar or confirmar[0] not in "sn":
                        continue
                    if confirmar[0] == "n":
                        menu = True
                        break

                    if self.uso and self.uso[0] in self.armadura:
                        if self.uso[0] == "capacete":
                            defesa = 4
                        elif self.uso[0] == "peitoral":
                            defesa = 7
                        else:
                            defesa = 0
                    elif self.uso and self.uso[0] in self.arma:
                        if self.uso[0] == "excalibur":
                            dano_a_mais = 5
                        elif self.uso[0] == "espada":
                            dano_a_mais = 3
                        elif self.uso[0] == "sabre":
                            dano_a_mais = 10
                        else:
                            dano_a_mais = 0
                    else:
                        defesa = 0
                        dano_a_mais = 0

                    if vida_player <= 0:
                        self.derrotado = True
                        menu = True
                        break

                    if vida_boss <= 0:
                        print("O player derrotou os monstros!!")
                        if vida_player >= 50 and "nem senti" not in self.conquistas:
                            self.conquistas.append("nem senti")
                        time.sleep(3)
                        item = random.randint(1, 50)
                        if item == 1 and "espada" not in self.itens:
                            self.conquistas.append("espada")
                            self.itens.append("espada")
                        elif item == 2 and "excalibur" not in self.itens:
                            self.conquistas.append("excalibur")
                            self.itens.append("excalibur")
                        elif item == 3 and "capacete" not in self.itens:
                            self.conquistas.append("capacete")
                            self.itens.append("capacete")
                        elif item == 4 and "peitoral" not in self.itens:
                            self.conquistas.append("peitoral")
                            self.itens.append("peitoral")
                        if (
                            all(x in self.conquistas for x in ("sabre", "espada", "excalibur", "capacete", "peitoral"))
                            and "Set completo" not in self.conquistas
                        ):
                            self.conquistas.append("Set completo")
                        combate_em_andamento = False
                        break

                    dado = random.randint(1, 20)
                    ataque_tipo = random.randint(1, 3)
                    if dado == 20 and "vinte natural" not in self.conquistas:
                        self.conquistas.append("vinte natural")

                    if self.uso and self.uso[0] in self.arma and dado == 20:
                        dano = 25 + dano_a_mais
                    else:
                        dano = dado + dano_a_mais

                    self.clear()
                    print("Ataque de player, jogando o dado...")
                    time.sleep(1.5)
                    print(dado)
                    time.sleep(1.5)
                    print(f"player deu {dano} de dano!")
                    time.sleep(3)

                    if sangramento:
                        self.clear()
                        print("Player está sangrando (-5)")
                        vida_player -= 5
                        print(f"\nPlayer está com {vida_player} de vida")
                        sangramento = False
                        time.sleep(3)

                    if vida_monstro > 0:
                        vida_monstro -= dano
                    else:
                        vida_boss -= dano

                    if vida_monstro > 0:
                        self.clear()
                        if vida_monstro <= 0:
                            print("Você derrotou o monstro!!")
                            time.sleep(3)
                            self.clear()
                            print("Espera!! Tem outro gigante bem ali!!")
                            if vida_player < 85:
                                vida_player += 15
                            time.sleep(3)
                        else:
                            print(f"O monstro está com {vida_monstro} de vida")
                            time.sleep(3)
                            self.clear()
                            if ataque_tipo == 1:
                                ataque = ["mordida", ataque_basico]
                            else:
                                ataque = ["soco", ataque_secundario]
                            print(f"Vez do monstro atacar... Monstro está usando {ataque[0]} ({ataque[1]} de dano)")
                            time.sleep(3)
                            vida_player = vida_player - ataque[1] + defesa
                            if ataque[0] == "mordida":
                                sangramento = True
                                vida_player -= 5
                                print("Player está sangrando (-5)")
                            self.clear()
                            print(f"Player está com {vida_player} de vida")
                            time.sleep(3)
                    else:
                        if vida_boss <= 0:
                            continue
                        self.clear()
                        print(f"O Boss está com {vida_boss} de vida")
                        time.sleep(3)
                        self.clear()
                        if ataque_tipo == 1:
                            ataque = ["mordida", ataque_basico]
                        elif ataque_tipo == 2:
                            ataque = ["soco", ataque_secundario]
                        else:
                            ataque = ["espancada", ataque_especial]
                        print(f"Vez do Boss atacar... Boss está usando {ataque[0]} ({ataque[1]} de dano)")
                        time.sleep(3)
                        vida_player = vida_player - ataque[1] + defesa
                        if ataque[0] == "mordida":
                            sangramento = True
                            vida_player -= 5
                            print("Player está sangrando (-5)")
                            time.sleep(3)
                        self.clear()
                        print(f"Player está com {vida_player} de vida")
                        time.sleep(3)

                    if vida_player <= 0:
                        self.derrotado = True
                        menu = True
                        break

                if menu:
                    return

                while True:
                    self.clear()
                    print("Você passou para a terceira fase do caminho do mal, parabéns!!")
                    continuar = self.leia_opcao("Pronto para o que há de vir? [S]im [N]ão ")
                    if not continuar or continuar[0] not in "sn":
                        continue
                    if continuar[0] == "n":
                        menu = True
                        break

                    moeda = "cara" if random.randint(1, 2) == 1 else "coroa"
                    escolha = self.leia_opcao("Faça a escolha certa:\nCara ou Coroa?\n")
                    if not escolha or escolha not in ("cara", "coroa"):
                        continue

                    if escolha == moeda:
                        self.clear()
                        print(
                            "Parabéns, você ganhou o caminho do mal! \nJunto disso ganhou também uma conquista e perda de tempo de vida"
                        )
                        if "Caminho do mal" not in self.conquistas:
                            self.conquistas.append("Caminho do mal")
                        if not self.passou:
                            if "first try" not in self.conquistas:
                                self.conquistas.append("first try")
                        self.passou = True

                        voltar = self.leia_opcao('Deseja voltar ao menu?\n(Se "não" você sairá do jogo) ')
                        if not voltar or voltar[0] not in "sn":
                            continue
                        if voltar[0] == "s":
                            return
                        else:
                            self.acabar = True
                            return
                    else:
                        self.derrotado = True
                        return

    def mostrar_regras(self):
        self.clear()
        print(
            "Para deixar mais claro, esse jogo possui algumas regras e explicações:\n"
            "\n1 - Acaso perder algum desafio, o jogo te trará para o menu."
            "\n2 - O nível do bem é mais fácil do que o nível do mal, \napesar disso, você dependerá MUITO da sua sorte para passar."
            "\n3 - Você pode ganhar itens que te ajudarão a derrotar os monstros\nNo caminho do mal."
            '\n4 - É possível "Platinar" o jogo, enquanto isso, o tempo corre.'
            "\n5 - O final do caminho do mal é desagradável."
            "\n6 - Há 17 conquistas no tal."
            "\n7 - Há uma conquista por fase, menos a primeria fase do mal."
            "\n8 - A chance de você conseguir todas as conqusitas do RPG\nÉ de 0,00000016... Boa sorte!"
        )
        voltar = self.leia_opcao('\nDigite "V" para voltar: ')

    def mostrar_conquistas(self):
        self.clear()
        print(f"Bem vindo a aba de conquistas, atualmente você possui {len(self.conquistas)}.")
        print(self.conquistas)
        voltar = self.leia_opcao('Digite "V" para voltar: ')

    def menu_itens(self):
        self.clear()
        print(f"Bem vindo a aba de itens, atualmente você possui {len(self.itens)}.")
        print(self.itens)
        equipar = self.leia_opcao(
            'Deseja equipar algum item?\n(Se sim, escrever o nome do item, se não, digite "não") '
        )
        if not equipar:
            return
        if equipar[0] == "n":
            return
        if equipar in self.uso:
            print("Item já está em uso")
            time.sleep(2)
            return
        if equipar not in self.itens:
            print("Você não tem este item para poder usa-lo")
            time.sleep(2)
            return

        if equipar in self.armadura or equipar in self.arma:
            if self.uso:
                self.uso[0:1] = [equipar]
            else:
                self.uso.append(equipar)
        else:
            return

        print(f"Item em uso: {self.uso}")
        voltar = self.leia_opcao('Digite "V" para voltar: ')

    def sair(self):
        self.clear()
        confirmar = self.leia_opcao("Deseja sair mesmo? [S]im [N]ão ")
        if not confirmar or confirmar[0] not in "sn":
            return
        if confirmar[0] == "s":
            self.clear()
            self.acabar = True


if __name__ == "__main__":
    jogo = JogoRPGSimples()
    jogo.menu_principal()
