from math import pow
print('='*50)
print('Calculador de IMC')
print('='*50)
peso = float(input('Informe o peso da pessoa: '))
altura = float(input('Informe a altura da pessoa: '))
imc = 0
if altura < 3:
   imc = peso / pow(altura, 2)
else:
    imc = peso / pow(altura/100, 2)
if imc < 18.5:
    print('O IMC da pessoa é {:.2f} e ela está abaixo do peso.'.format(imc))
elif imc < 25:
    print('O IMC da pessoa é {:.2f} e ela está com o peso ideal'.format(imc))
elif imc < 30:
    print('O IMC da pessoa é {:.2f} e ela está com sobrepeso'.format(imc))
elif imc < 40:
    print('O IMC da pessoa é {:.2f} e ela está com obesidade'.format(imc))
else:
    print('O IMC da pessoa é {:.2f} e ela está com obesidade mórbida'.format(imc))
print('='*50)
print('Fim do programa')
print('='*50)