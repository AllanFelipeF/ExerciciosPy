from datetime import date
ano = int(input('Digite o ano que quer analisar, ou digite 0 para saber do ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bisexto'.format(ano))
else:
    print('O ano {} não é bisexto'.format(ano))
print('Fim do programa')