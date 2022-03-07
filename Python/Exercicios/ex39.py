from datetime import date
print('='*20)
print('Programa de alistamento')
print('='*20)
hoje = date.today().year
anoNasc = int(input('Informe o ano de nascimento: '))
idade = hoje - anoNasc 
if idade < 18:
    print('O jovem nascido em {} ainda irá se alistar, faltam {} anos para ele se alistar'.format(anoNasc, 18 - idade))
elif idade > 18:
    print('O jovem nascido em {} precisa se alistar pois já passou do tempo para se alistar, a diferença é de {} anos'.format(anoNasc, idade - 18))
else:
    print('O jovem nascido em {} ja pode se alistar.'.format(anoNasc))
print('='*20)
print('Fim do programa')
print('='*20)