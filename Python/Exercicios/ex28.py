from random import randint
num = randint(0, 5)
adv = int(input('Pensei em um numero, tente adivinhar: '))
if num == adv:
    print('Parabéns!!! Você ganhou!')
else:
    print('Errou!!! O Computador ganhou!')
print('Fim de jogo')
