peso = 0
maiPeso = 0
menPeso = 0
for i in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maiPeso = peso
        menPeso = peso
    else:
        if peso > maiPeso:
            maiPeso = peso
        if peso < menPeso:
            menPeso = peso
print('O Maior peso é {} e o menor é {}'.format(maiPeso, menPeso))