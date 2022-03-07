print('='*20)
print('Calculador de média')
print('='*20)
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('O aluno teve a média de {} e foi reprovado'.format(media))
elif media >= 5 and media < 7:
    print('A média do aluno foi {} e ele está de recuperação'.format(media))
else:
    print('A média do aluno foi {} e ele foi aprovado!'.format(media))
print('='*20)
print('Fim do programa')
print('='*20)