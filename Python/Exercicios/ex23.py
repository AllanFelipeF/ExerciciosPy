num = int(input('Digite um numero de 0 a 9999: '))
unit = num % 10
deze = num // 10 % 10
cent = num // 100 % 10
milh = num // 1000 % 10
print('Unidade: {}'.format(unit))
print('Dezena: {}'.format(deze))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(milh))