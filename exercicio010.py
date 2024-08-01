dinheiro = float(input('Quanto de dinheiro você tem na carteira? '))
cotacao_dolar = 5.67

quantidade_dolares = dinheiro / cotacao_dolar

print(f'A cotação atual do dólar em reais é: R${cotacao_dolar}')
print(f'Com R${dinheiro:.2f} você pode comprar ${quantidade_dolares:.2f} dólares')
