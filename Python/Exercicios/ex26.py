frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira vez que ela aparece é na {}ª posição'.format(frase.find('A')))
print('A ultima vez que ela aparece é na {}ª posição'.format(frase.rfind('A')))