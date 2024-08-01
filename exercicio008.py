distancia = float(input('Digite a distância em metros: '))

print(f'''
    A media de {distancia:.1f}m corresponde a :
    {distancia/1000} km
    {distancia/100} hm
    {distancia/10} dam
    {distancia*10} dm
    {distancia*100} cm
    {distancia*1000} mm

''')