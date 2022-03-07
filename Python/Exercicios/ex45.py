from random import choice
from time import sleep
print('='*50)
print('Pedra, Papel e Tesoura')
print('='*50)
jokenpoPc = [1, 2, 3]
computador = choice(jokenpoPc)
jokenpoHn = int(input('Selecione:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nSeleção: '))
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
if jokenpoHn == computador:
    print('Deu empate')
elif computador == 1 and jokenpoHn == 2:
    print('O computador escolheu pedra, você ganhou!!!')
elif computador == 1 and jokenpoHn == 3:
    print('O computador escolheu pedra, você perdeu!!!')
elif computador == 2 and jokenpoHn == 1:
    print('O computador selecionou papel, você perdeu!!!')
elif computador == 2 and jokenpoHn == 3:
    print('O computador escolheu papel, você ganhou!!!')
elif computador == 3 and jokenpoHn == 1:
    print('O computador escolheu tesoura, você ganhou!!!')
elif computador == 3 and jokenpoHn == 2:
    print('O computador escolheu tesoura, você perdeu!!!')
else:
    print('Seleção inválida')
print('='*50)
print('Fim do programa')
print('='*50)