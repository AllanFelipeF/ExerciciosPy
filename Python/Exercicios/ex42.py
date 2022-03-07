print('='*20)
print('Analisador de Triângulos V2')
print('='*20)
r1 = float(input('Informe o primeiro seguimento: '))
r2 = float(input('Informe o segundo seguimento: '))
r3 = float(input('Informe o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos formam um triângulo!!!')
    if r1 == r2 and r1 == r3:
        print('As retas formam um triângulo Equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('As retas formam um triangulo Isósceles!')
    else:
        print('As retas formam um triângulo Escaleno!')
else:
    print('As retas não formam um triângulo')
print('='*20)
print('Fim do programa')
print('='*20)