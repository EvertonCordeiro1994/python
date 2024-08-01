import math

num = int(input('Digite um número: '))

print(f'''
    O dobro de {num} é {num*2}
    O triplo de {num} é {num*3}
    A raíz quadrada de {num} é {math.sqrt(num):.1f}
''')