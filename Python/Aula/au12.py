nome = str(input('Qual teu nome? ')).strip()
if nome == 'Allan':
    print('Nice name bro!!!')
elif nome == 'Pedro' or name == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem normal')
else:
    print('Nome comum!')
print('Tenha um bom dia {}'.format(nome))