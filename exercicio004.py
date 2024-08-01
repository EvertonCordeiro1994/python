entrada = input('Digite algo: ')

print(f'''
O tipo primitivo é {type(entrada)}
Só tem espaços? {entrada.isspace()}
É numérico? {entrada.isnumeric()}
É alfabético? {entrada.isalpha()}
É alfanumérico? {entrada.isalnum()}
Está em maiúsculas? {entrada.isupper()}
Está em minúsculas? {entrada.islower()}
Está capitalizada? {entrada.istitle()}
''')
