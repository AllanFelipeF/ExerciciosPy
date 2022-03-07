frase = str(input('Digite uma frase: ')).strip().upper()
fn = frase.replace(' ', '')
inversao = ''
for i in range(len(fn) - 1, -1, -1):
    inversao += fn[i]
if inversao == fn:
    print('A frase {} é um palíndromo!'.format(frase))
else:
    print('A frase {} não é um palíndromo!'.format(frase))