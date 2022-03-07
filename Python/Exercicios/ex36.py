print('='*20)
print('Aluguel de casas')
print('='*20)
valorCasa = float(input("Informe o valor da casa: "))
salario = float(input('Informe o salário bruto: '))
totAnos = int(input('Informe em quantos anos a casa será paga: '))
prestMensal = valorCasa / (totAnos * 12)
if prestMensal > salario * 0.3:
    print('Infelizmente a casa não podera ser comprada.')
else: 
    print('O valor da parcela da casa em {} anos sera de R${:.2f} por mes'.format(totAnos, prestMensal))
print('Fim do programa')