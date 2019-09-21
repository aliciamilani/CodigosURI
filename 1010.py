lista = input().split(' ')

cod = float(lista[0])
num = float(lista[1])
unitario = float(lista[2])

lista = input().split(' ')

cod2 = float(lista[0])
num2 = float(lista[1])
unitario2 = float(lista[2])

valor = (num*unitario) + (num2*unitario2)

print("VALOR A PAGAR: R$ %.2f"%valor)