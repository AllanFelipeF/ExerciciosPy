a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))
c = float(input('Digite um terceiro numero: '))
menor = a
maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero é {} e o menor é {}'.format(menor, maior))
print('Fim do programa')