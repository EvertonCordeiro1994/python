import random


nome01 = input('Digite o primeiro nome: ')
nome02 = input('Digite o seguno nome: ')
nome03 = input('Digite o terceiro nome: ')
nome04 = input('Digite o quarto nome: ')


lista_de_nomes = [nome01,nome02,nome03,nome04]

embaralhador = random.shuffle(lista_de_nomes)

print(f'O nome escohido foi {lista_de_nomes} ')