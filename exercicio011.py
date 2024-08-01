# 2mts² = 1lt de tinta


largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura*altura

print(f'Sua parade tem a dimensão de {altura:.2f} X {largura:.2f} sua area é de {area:.2f} ')
print(f'Para pintar toda a sua parede, você vai precisar de {(area/2):.2f}lts de tinta')

