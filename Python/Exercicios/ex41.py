from datetime import date
print('='*20)
print('Classificador de Nadadores')
print('='*20)
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - anoNasc
if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e está na categoria JUNIOR'.format(idade))
elif idade <= 20:
    print('O atleta tem {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER'.format(idade))
print('='*20)
print('Fim do programa')
print('='*20)