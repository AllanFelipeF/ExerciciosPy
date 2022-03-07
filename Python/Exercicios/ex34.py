sal = float(input('Digite o salario: '))
novosal = 0
if sal > 1250:
    novosal = sal + sal * 0.10
    print('O novo salário com aumento de 10% sera de: R${:.2f}'.format(novosal))
else:
    novosal = sal + sal * 0.15
    print('O novo salario com aumento de 15% sera de: R${:.2f}'.format(novosal))
print('Fim do programa')