nome = input('Digite seu nome: ')

print(f'''
    Seu nome em maiúsculo fica  { nome.upper()}
    Seu nome em minúsculo fica  { nome.lower()}
    Seu nome tem {len(nome.replace(' ',''))} letras
    Seu primeiro nome tem {len(nome.split()[0])} letras

''')