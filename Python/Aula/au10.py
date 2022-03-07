nome = str(input('Qual é seu nome: ')).strip().title()
if nome == 'Allan':
    print('Que nome foda')
else:
    print('Que nome bosta!')
print('Bom dia {}'.format(nome))