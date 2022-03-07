from time import sleep
val1 = float(input('Digite um valor: '))
val2 = float(input('Digite um valor: '))
menu = 0
while menu != 5:
    print(''' 
Selecione uma das opções:
    1 - Somar
    2 - Multiplicar
    3 - Maior
    4 - Novos números
    5 - Sair do programa''')
    menu = int(input('Seleção: '))
    if menu == 1:
        print('A soma dos valores {} e {} é: {}'.format(val1, val2, val1 + val2))
        sleep(2)
    elif menu == 2:
        print('A multiplicação de {} e {} é: {}'.format(val1, val2, val1 * val2))
        sleep(2)
    elif menu == 3:
        if val1 > val2:
            print('O valor {} é maior que o valor {}'.format(val1, val2))
            sleep(2)
        elif val2 > val1:
            print('O valor {} é maior que o valor {}'.format(val2, val1))
            sleep(2)
        else:
            print('Os valores são iguais!')
            sleep(2)
    elif menu == 4:
        val1 = float(input('Digite um valor: '))
        val2 = float(input('Digite um valor: '))
    elif menu == 5:
        print('Fim do programa')
    else:
        print('Valor inválido tente novamente!!!')
        sleep(2)

