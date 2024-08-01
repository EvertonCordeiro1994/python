import math

cateto_oposto = float(input('Digite o valor do cateto oposto: '))

cateto_adjasente = float(input('Digite o valor do cateto adjasente: '))

hipotenusa = math.sqrt((cateto_oposto**2) + (cateto_adjasente**2))

print(f'A hipotenusa vai medir {hipotenusa:.2f}')

