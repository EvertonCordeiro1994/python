numero_digitado = int(input('Digite um número de 0 a 9999: '))

formatado = f'{numero_digitado:04d}'

print(f'''
    unidade = { formatado[3]}
    dezena  = { formatado[2]}
    centena = { formatado[1]}
    milhar  = { formatado[0]}
''')

