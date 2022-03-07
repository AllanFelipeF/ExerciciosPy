nome = str(input('Digite seu nome completo: ')).strip()
nomespl = nome.split()
print('O seu nome é: {} \nO seu primeiro nome é: {} \nE seu ultimo nome é: {}'.format(nome, nomespl[0], nomespl[len(nomespl)-1]))