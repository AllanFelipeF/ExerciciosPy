city = str(input('Digite o nome da cidade: ')).strip()
fcity = city.upper().split()
print('A cidade {} começa com o nome SANTO? {}'.format(city, 'SANTO' in fcity[0]))