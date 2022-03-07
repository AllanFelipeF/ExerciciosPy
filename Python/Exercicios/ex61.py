pt = int(input('Digite o primeiro termo da P.A: '))
raz = int(input('Digite a razão da P.A: '))
dec = pt + (10 - 1) * raz
n = pt
if raz == 0:
    while n < 10:
        print('{}'.format(pt), end=' → ')
        n += 1
else:
    while n < dec + 1:
        print('{}'.format(n), end=' → ')
        n += raz
print('Fim da P.A')