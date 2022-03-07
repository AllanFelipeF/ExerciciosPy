print('='*20)
print('Verificador maior e menor')
print('='*20)
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 > num2:
    print('O primeiro número {} é maior que o segundo número {}'.format(num1, num2))
elif num2 > num1:
    print('O segundo número {} é maior que o primeiro número {}'.format(num2, num1))
else:
    print('Não existe valor maior, os números {} e {} são iguais: '.format(num1, num2))
print('='*20)
print('Fim do programa')
print('='*20)