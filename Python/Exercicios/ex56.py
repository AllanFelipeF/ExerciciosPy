nome = ''
idade = 0
sexo = ''
somam = 0
maisveih = 0
nomemaisvei = ''
mumen20 = 0
for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i))).strip().capitalize()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    somam += idade
    if sexo == 'M' and idade > maisveih:
        nomemaisvei = nome
        maisveih = idade
    if sexo == 'F' and idade < 20:
        mumen20 += 1
print('Á média de idade do grupo é: '.format(somam/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maisveih, nomemaisvei))
print('O número de mulheres menores que 20 anos são {} mulheres'.format(mumen20))