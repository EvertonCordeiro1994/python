import math


angulo_digitado = float(input('Digite o ângulo a ser calculado: '))

angulo_radiano = math.radians(angulo_digitado)

print(f'''
    O ângulo {angulo_digitado}º tem 
    {math.sin(angulo_radiano):.2f} de seno
    {math.cos(angulo_radiano):.2f} de cosseno
    {math.tan(angulo_radiano):.2f} de tangente
''')