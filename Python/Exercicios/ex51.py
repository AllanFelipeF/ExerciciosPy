pt = int(input('Digite o primeiro termo da P.A: '))
raz = int(input('Digite a razão da P.A: '))
dec = pt + (10-1) * raz
if raz == 0:
    for i in range(0,10):
        print('{}'.format(pt), end=' → ')
else:
    for i in range(pt, dec, raz):
        print('{}'.format(i), end=' → ')
print('Fim da P.A')