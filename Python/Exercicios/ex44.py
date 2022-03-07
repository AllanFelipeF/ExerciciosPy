print('='*50)
print('Gerenciador de Pagamentos')
print('='*50)
precoProd = float(input('Informe o valor do produto: '))
formaPag = int(input('Selecione:\n1 - À vista Dinheiro/Cheque\n2 - À vista no cartão\n3 - Até 2x no cartão\n4 - 3x ou mais no cartão\nSeleção: '))
precoFinal = 0
parcelas = 0
if formaPag == 1:
    precoFinal = precoProd - precoProd * 0.10
    print('Você selecionou o valor a vista, terá um desconto de 10%, o valor de {:.2f} ficara: R${:.2f}'.format(precoProd, precoFinal))
elif formaPag == 2:
    precoFinal = precoProd - precoProd * 0.05
    print('Você seleciou a vista no cartão, terá o desconto de 5%, o valor de {:.2f} ficara: R${:.2f}'.format(precoProd, precoFinal))
elif formaPag == 3:
    parcelas = 2
    print('Você pagara 2 parcelas de R${:.2f}'.format(precoProd / parcelas))
    print('Você escolheu fazer em 2x no cartão, o valor será: R${:.2f}'.format(precoProd))
elif formaPag == 4:
    precoFinal = precoProd + precoProd * 0.2
    parcelas = int(input('Infomre a quantidade de parcelas: '))
    print('Você pagará {} parcelas de R${:.2f}'.format(parcelas, precoFinal / parcelas))
    print('Você escolheu 3x ou mais, o valor tera um acréscimo de 20%, o valor de R${:.2f} ficara por: R${}'.format(precoProd, precoFinal))
else:
    print('Seleção incorreta!!')
print('='*50)
print('Fim do programa')
print('='*50)