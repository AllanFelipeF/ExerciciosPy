num = 0
soma = 0
total = 0
while num != 999:
    num = int(input('Digite um valor para soma, caso queira parar digite 999: '))
    if num != 999:
        soma += num
        total += 1
print('Você digitou {} números e a soma de todos é: {}'.format(total, soma))