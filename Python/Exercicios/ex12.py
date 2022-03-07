valor = float(input('Digite o valor do produto: '))
desc = valor - valor * 0.05
print('O produto de R${:.2f} sai por R${:.2f} na promoção'.format(valor, desc))