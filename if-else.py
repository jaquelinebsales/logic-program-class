continuar = 's'

while (continuar.upper() in "SY"):
    nome = input('Digite seu nome: ')
    nome = nome.capitalize()
    idade = int(input('Digite sua idade: '))

    if idade >= 0 and idade < 13:
        print(f'{nome}, você é criança')
    if idade < 18:
        print(f'{nome}, você é adolescente')
    elif idade < 60:
        print(f'{nome}, você é um adulto')
    elif idade > 60:
        print(f'{nome}, você é um idoso')
    else:
        print('Valor inválido')
    
    continuar = input("Deseja continuar? ")
