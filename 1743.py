lista1 = []
lista2 = []
situacao = True

a = input("").split(" ")
lista1.append(a[0])
lista1.append(a[1])
lista1.append(a[2])
lista1.append(a[3])
lista1.append(a[4])

b = input("").split(" ")
lista2.append(b[0])
lista2.append(b[1])
lista2.append(b[2])
lista2.append(b[3])
lista2.append(b[4])


for i in range(5):
    if(lista1[i] == lista2[i]):
        situacao = False
        break

if(situacao == True):
    print('Y')
else:
    print('N')
    