#Calcule baskhara
'''def baskhara(a, b, c):
    positivo, negativo = (-b + ((b**2 - (4*a*c))**0.5)) /2*a, (-b - ((b**2 - (4*a*c))**0.5)) /2*a
    return positivo, negativo

a = int(input('Calculadora de baskhara\nValor a: '))
b = int(input('Valor b: '))
c = int(input('Valor c: '))

positivo, negativo = baskhara(a, b, c)

print(f'x¹ = {positivo:.2f}\nx² = {negativo:.2f}')'''

#Teste de sorte - Rode o código uma vez para ver o resultado
'''import random
import time

player = 100
monstros = 20
contagem = 0
turno = True

def sorte():
    global player, monstros, contagem, turno

    while player > 0:
        if turno:
            ataque = random.randint(1,20)
            monstros -= ataque
        else:
            ataque = random.randint(1,10)
            player -= ataque
        if monstros <= 0:
            contagem +=1
            monstros = 20
        if turno:
            turno = False
        else:
            turno = True

    return contagem

if sorte() > 7:
    print('você está com sorte')
elif sorte() < 7:
    print('você está com azar')
else:
    print('você está com sua sorte normalizada')'''

#exercício funções

'''def multi_nao_nomeados(*args):
    total = 1
    for i in args:
        total *= i

    def par_impar(total):
        return total % 2 == 0

    par_impar = par_impar(total)

    return total, par_impar

resultados = multi_nao_nomeados(1, 7, 5, 3, 2)
print(f'O produto dos valores é {resultados[0]}\nO produto é', 'par' if resultados[1] else 'ímpar')'''

#Gerador e validador de cpf
'''import random
import os
import pyperclip

def validador_cpf(cpf):
    regressivo = 10
    validador = cpf[:9]

    for i in range(0, 2):
        digitos = 0

        for i in validador:
            digitos = (int(i) * regressivo) + digitos
            regressivo -= 1

        digitos = digitos % 11

        if str(digitos) in "10":
            verificador = 0
        else:
            verificador = 11 - digitos

        regressivo = 11
        validador += str(verificador)

    return validador

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
while True:
    escolha = input("1) Gerar CPF \t2)Validar CPF\nEscolha: ")
    if escolha == '1':
        limpar()
        cpf = ''
        for i in range(9):
            cpf += str(random.randint(0,9))
        cpf = validador_cpf(cpf)
        pyperclip.copy(cpf)
        print(f'CPF gerado: {cpf}\n(Copiado automaticamente)')
    elif escolha == '2':
        limpar()
        cpf = input("Digite um CPF: ").replace('-', '').replace('.', '')

        if validador_cpf(cpf) == cpf:
            print("CPF válido")
        else:
            print("CPF inválido")
    else:
        limpar()
        break
'''

#Gerador e validador de CNPJ(Alphanumérico):
...
