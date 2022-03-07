dias = int(input('Digite quantos dias o carro será alugado: '))
km = float(input('Digite quantos Km foram percorridos pelo veículo: '))
preco = dias * 60 + km * 0.15
print('O carro alugado por {} dias que percorreu {}Km tera o aluguel de R${:.2f}'.format(dias, km, preco))