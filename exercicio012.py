valor_produto = float(input('Digite o valor do produto: '))
desconto = (valor_produto/100)*5
valor_final = valor_produto - desconto

print(f'O produto que custa R${valor_produto}, com desconto de 5% fica no valor de R${valor_final:.2f}')