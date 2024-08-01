multiplicador = int(input('Digite um número inteiro para ver a sua tabuada: '))

print(f'Tabuada do {multiplicador}')
print('-'*15)
for i in range(0,11) : 
    if i < 10:
         print(f'{multiplicador} X 0{i} = {multiplicador*i}') 
    else:
        print(f'{multiplicador} X {i} = {multiplicador*i}')

print('-'*15)