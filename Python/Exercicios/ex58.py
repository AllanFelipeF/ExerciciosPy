from random import randint
computador = randint(0, 10)
jogador = ''
erros = 0
while computador != jogador:
    jogador = int(input('Escolhi um número inteiro de 0 a 10, tente adivinhar: '))
    if computador == jogador:
        print('Parabéns!!! Você acertou, eu estava pensando em {} mesmo!!!'.format(computador))
        print('Você errou {} vezes'.format(erros))
    else:
        print('Errou!!! Você precisa acertar o número tente novamente!!!')
        erros += 1
print('Fim da execução')