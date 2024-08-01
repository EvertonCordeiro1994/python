#dia = 60
#km = 0.15


dias_com_o_carro = int(input('Digite quantos dias você ficou com o carro: '))

km_rodados = float(input('Digite quantos kms você andou com o carro: '))

calculo_diaria = dias_com_o_carro * 60

calculo_km = km_rodados * 0.15

valor_a_pagar = calculo_diaria + calculo_km

print(f'''
    você ficou {dias_com_o_carro} dias com o carro,
    Rodou {km_rodados}kms, entao deve pagar
    R${valor_a_pagar:.2f}
''')