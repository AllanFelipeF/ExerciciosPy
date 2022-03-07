km = float(input('Qual a distancia da viagem? '))
if km <= 200:
    valor = km*0.50
    print('O valor a ser cobrado pela viagem de {}Km será: R${:.2f}'.format(km, valor))
else:
    valor = km*0.45
    print('O valor a ser cobrado pela viagem de {}Km será: R${:.2f}'.format(km, valor))
print('Fim do programa')