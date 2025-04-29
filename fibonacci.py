n1 = 1
n2 = 1
print(n1)
print(n2)
for i in range(1, 12): 
    proximo = n1 + n2
    n2 = n1
    n1 = proximo
    print(proximo)
