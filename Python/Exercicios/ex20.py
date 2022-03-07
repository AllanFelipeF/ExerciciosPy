from random import shuffle
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
allist = [al1, al2, al3, al4]
shuffle(allist)
print('A ordem de alunos para fazer as apresentações será: \n{}'.format(allist))