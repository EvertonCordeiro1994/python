import random


nome01 = input('Digite o primeiro nome: ')
nome02 = input('Digite o seguno nome: ')
nome03 = input('Digite o terceiro nome: ')


lista_de_nomes = [nome01,nome02,nome03]

escolha = random.randint(0,2)

print(f'O nome escohido foi {lista_de_nomes[escolha]} ')