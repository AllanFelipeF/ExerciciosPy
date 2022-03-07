print('='*20)
print('Conversor de bases')
print('='*20)
num = int(input('Digite um número inteiro para conversão: '))
escolha = int(input('Selecione:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nSeleção: '))
if escolha == 1:
    print('O número {} em Binário é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} em Octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} em Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!!!')
print('='*20)
print('Fim do programa')
print('='*20)
