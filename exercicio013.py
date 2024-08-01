salario_atual = float(input('Digite o salário atual: '))
aumento = (salario_atual/100)* 15
salario_atualizado = salario_atual + aumento

print(f'O funcionário que recebia R${salario_atual}, com um aumento de 15% vai passar a receber {salario_atualizado}')