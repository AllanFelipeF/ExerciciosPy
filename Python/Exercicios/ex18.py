from math import sin, cos, tan, radians, trunc
ang = float(input('Digite o angulo para ver seu seno, coseno e tangente: '))
sen = sin(radians(ang))
cosen = cos(radians(ang))
tang = tan(radians(ang))
print('O angulo de {}º tem o seno de {:.2f} o coseno de {:.2f} e a tangente de {:.2f}'.format(trunc(ang), sen,cosen,tang))