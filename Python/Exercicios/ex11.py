larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
tinta = 2
print('Para pintar a parede de {}m² são necessários {:.2f}L de tinta'.format(alt*larg, (alt*larg)/tinta))