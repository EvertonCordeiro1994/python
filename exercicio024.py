nome_da_cidade = input('Digite o nome de uma cidade: ')

if 'SANTO' in nome_da_cidade.split()[0].upper():
    print(f'{nome_da_cidade} começa com SANTO')
else:
    print(f'{nome_da_cidade} não começa com SANTO')

