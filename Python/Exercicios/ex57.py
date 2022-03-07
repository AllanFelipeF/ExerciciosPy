sexo = ''
n = 1
while n != 0:
    sexo = str(input('Digite o seu sexo[M/F]: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Sexo confirmado!')
        n = 0
    else:
        print('Valor incorreto, digite novamente!')
print('Fim da execução')