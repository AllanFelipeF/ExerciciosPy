nasc = 0
maitot = 0
mentot = 0
for i in range(0, 7):
    nasc = int(input('Digite a idade para verificação: '))
    if nasc < 21:
        mentot += 1
    else:
        maitot += 1
print('O numero de pessoas maior de idade é {} e menores são {}'.format(maitot, mentot))