n1 = int(input('Digite um valor para fatorial: '))
fac = 1
n = n1
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fac *= n
    n -= 1
print('{}'.format(fac))