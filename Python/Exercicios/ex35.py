lado1 = float(input('Digite o primeiro seguimento: '))
lado2 = float(input('Digite o segundo seguimento: '))
lado3 = float(input('Digite o terceiro seguimento: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Esses seguimentos formam um triangulo!')
else:
    print('Esses seguimentos não formam um triangulo!')