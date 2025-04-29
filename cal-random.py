from random import randint
n = 0
soma = 0
maior = -9999
menor = 9999
for i in range(0,10):
    n = randint(0,20)
    print(n)
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma += n
        
    
print(f"O menor número é:{menor}")
print(f"O maior número é:{maior}")
print(f"A diferença entre eles é:{maior - menor}")
print(f"A média é:{soma/20}")
