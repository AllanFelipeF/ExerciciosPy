vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80)*7
    print('Você foi multado em: R${:.2f}'.format(multa))
print('Fim do programa')
